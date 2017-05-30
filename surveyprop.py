import sys
import copy
import numpy as np
import numpy.random as npr
import random
import pprint

global_state = {}

"""
sort of a port of the mezard et al collab's c implementation
nontrivial changes, tho
"""

def incr(parent, key):
    """ mutates """
    if key not in parent:
        parent[key] = 0
    parent[key] += 1

def generate_random_instance(num_clauses, num_variables, k):
    """
    I am still not sure about this fucking thing
    go painstakingly line by line and assure self of correctness of generated one
    """
    assert num_variables >= k
    global global_state
    global_state["clause_categories"] = [0 for _ in xrange(k+1)]
    global_state["clause_categories"][k] = num_clauses
    global_state["max_literals"] = k
    global_state["free_spin"] = num_variables
    clauses, variables = [{} for _ in xrange(num_clauses)], [{} for _ in xrange(num_variables + 1)]
    global_state["max_num_conns"] = 0
    """ make clause datastruct """
    for clause_idx in xrange(num_clauses):
        clauses[clause_idx]["type"] = k
        clauses[clause_idx]["lits"] = k
        clauses[clause_idx]["literal"] = [{} for _ in xrange(k)]
        for curr_lit in xrange(k):
            while True:
                randvar = random.randint(1, num_variables)
                used = any(randvar == literal.get("var", -1) for literal in clauses[clause_idx]["literal"])
                if not used:
                    break
            clauses[clause_idx]["literal"][curr_lit]["var"] = randvar
            clauses[clause_idx]["literal"][curr_lit]["bar"] = random.randint(0, 1)
            clauses[clause_idx]["literal"][curr_lit]["eta"] = random.random()
            incr(variables[randvar], "clauses")
            if variables[randvar]["clauses"] > global_state["max_num_conns"]:
                global_state["max_num_conns"] = variables[randvar]["clauses"]
    """ count up var datastruct """
    for var_idx in xrange(1, num_variables+1):
        variables[var_idx]["spin"] = 0
        variables[var_idx]["pi"] = {"p": 0, "m": 0}
        if variables[var_idx]["clauses"]:
            variables[var_idx]["clauselist"] = [{} for _ in xrange(variables[var_idx]["clauses"])]
            variables[var_idx]["clauses"] = 0
    """ fill up var datastruct """
    for clause_idx in xrange(num_clauses):
        for curr_lit in xrange(k):
            curr_var_idx = clauses[clause_idx]["literal"][curr_lit]["var"]
            curr_var = variables[curr_var_idx]
            curr_var["clauselist"][curr_var["clauses"]]["clause"] = clauses[clause_idx]
            curr_var["clauselist"][curr_var["clauses"]]["lit"] = curr_lit
            curr_var["clauses"] += 1
    return variables, clauses

def fix(variables, var_idx, spin):
    global global_state
    global_state["free_spin"] -= 1
    if variables[var_idx]["spin"]:
        return 1
    variables[var_idx]["spin"] = spin
    return simplify(variables, var_idx)

def simplify(variables, var_idx):
    global global_state
    # for(cl=0; cl<v[var].clauses; cl++) {
    #     c=v[var].clauselist[cl].clause;
    #     l=v[var].clauselist[cl].lit;
    #     if(c->type==0) {
    #         continue;
    #     }
    #     ncl[c->type]--;
    #     //check if var renders SAT the clause
    #     if(c->literal[l].bar==(v[var].spin==-1)) {
    #         ncl[0]++;
    #         c->type=0;
    #        continue;

    #     }
    #     ncl[(--(c->type))]++;
    #     //otherwise, check for further simplifications
    #     //type 0, contradiction?:
    #     if(c->type==0) {
    #         printf("contradiction\n");
    #         writeformula(fopen("contradiction.tmp.cnf","w+"));
    #         exit(-1);
    #     }
    #     //no contradiction
    #     //type 1: unit clause propagation
    #     if(c->type == 1) {
    #     //find the unfixed literal
    #         for(i=0; i<c->lits; i++) {
    #             if(v[aux=c->literal[i].var].spin==0)
    #                 break;
    #         }
    #         if(i==c->lits)
    #             continue;
    #     //a clause could be unit-clause-fixed by two different paths
    #         if(fix(aux,c->literal[i].bar?-1:1))
    #             return -1;
    #     }
    return 0


def randomize_eta():
    """ not needed in this impl yet, since we're only implementing random ksat"""
    raise NotImplemented()

def compute_pi():
    pass

def update_eta(clause_idx):
    pass

def compute_field(var_idx):
    pass

def fix_balanced():
    pass

def fix_chunk(num_chunks):
    pass

def iterate():
    pass

def compute_sigma():
    pass

def sequential_converge():
    pass

if __name__ == "__main__":
    """
    many things are 1-indexed here, and room left for the 1-indexing.
    this is because it's a python port of a c port of a fortran original program
    god is dead
    """
    num_clauses, num_variables, k = 6, 4, 3
    variables, clauses = generate_random_instance(num_clauses, num_variables, k)
    pp = pprint.PrettyPrinter(indent=2)
    # print "==============="
    # pp.pprint(clauses)
    # print "==============="
    # pp.pprint(variables)
    # print "==============="
    # print max_num_conns
