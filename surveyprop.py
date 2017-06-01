import sys
import copy
import numpy as np
import numpy.random as npr
import random
import pprint

global_state = {}
variables = None
clauses = None
prods = None

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
    global global_state, clauses, variables
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
    """ mutates """
    global variables
    for curr_var in variables[1:]:
        if curr_var["spin"] == 0:
            curr_var["pi"]["p"] = 1
            curr_var["pi"]["m"] = 1
            for curr_clause in curr_var["clauselist"]:
                if curr_clause["clause"]["type"]:
                    curr_literal = curr_clause["clause"]["literal"][curr_clause["lit"]]
                    if curr_literal["bar"]:
                        curr_var["pi"]["p"] *= 1 - curr_literal["eta"]
                    else:
                        curr_var["pi"]["m"] *= 1 - curr_literal["eta"]

def update_eta(clause_idx):
    global variables, clauses, prods, global_state
    if not prods:
        prods = [0 for _ in xrange(global_state["max_literals"])]
    curr_clause = clauses[clause_idx]
    zeroes = 0
    norho = 1
    allprod = 1.0
    for idx, curr_literal in enumerate(curr_clause["literal"]):
        if variables[curr_literal["var"]]["spin"] == 0:
            pi = variables[curr_literal["var"]]["pi"]
            if curr_literal["bar"]:
                w_t = pi["m"]
                w_n = pi["p"] / ((1.0 - curr_literal["eta"]) * (1.0 - (w_t * norho)))
            else:
                w_t = pi["p"]
                w_n = pi["m"] / ((1.0 - curr_literal["eta"]) * (1.0 - (w_t * norho)))
            prods[idx] = w_n / (w_n + w_t)
            if prods[idx] < 1e-16:
                zeroes += 1
                if zeroes == 2:
                    break
            else:
                allprod *= prods[idx]
    eps = 0
    for idx, curr_literal in enumerate(curr_clause["literal"]):
        if variables[curr_literal["var"]]["spin"] == 0:
            if not zeroes:
                new_eta = allprod / prods[idx]
            elif zeroes == 1 and prods[idx] < 1e-16:
                new_eta = allprod
            else:
                new_eta = 0.0

            pi = variables[curr_literal["var"]]["pi"]
            if curr_liberal["bar"]:
                pi["p"] = (1.0 - new_eta) / (1.0 - curr_literal["eta"])
            else:
                pi["m"] = (1.0 - new_eta) / (1.0 - curr_literal["eta"])

            if eps < np.abs(curr_literal - new_eta):
                eps = np.abs(curr_literal - new_eta)

            curr_literal["eta"] = new_eta
    return eps

def compute_field(var_idx):
    pass

def fix_balanced():
    pass

def fix_chunk(num_chunks):
    pass

def compute_sigma():
    pass

def sequential_converge(num_iters):
    global clauses
    compute_pi()
    idxs = range(len(clauses))
    for idx in xrange(num_iters):
        """ iterate() now folded into here: """
        curr_clause_idx = random.choice(idxs)
        update_eta(curr_clause_idx)

if __name__ == "__main__":
    """
    many things are 1-indexed here, and room left for the 1-indexing.
    this is because it's a python port of a c port of a fortran original program
    god is dead
    """
    num_clauses, num_variables, k = 6, 4, 3
    generate_random_instance(num_clauses, num_variables, k)
    sequential_converge(5000)
    pp = pprint.PrettyPrinter(indent=2)
    print "==============="
    pp.pprint(clauses) # eventually just print etas?
