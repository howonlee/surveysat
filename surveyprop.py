import sys
import copy
import numpy as np
import numpy.random as npr
import random

"""
void randomformula(int K)
//random k-sat formula
{
    for(var=1; var<=N; var++) if(v[var].clauses){
        v[var].clauselist=allclauses;
        allclauses+=v[var].clauses;
        v[var].clauses=0;
    }
    for(i=0; i<M; i++) {
        for(j=0; j<K; j++) {
            var=clause[i].literal[j].var;
            v[var].clauselist[v[var].clauses].clause=clause+i;
            v[var].clauselist[v[var].clauses++].lit=j;
        }
    }
    maxlit=K;
    freespin=N;
}

"""

def fix(var_idx, spin):
    pass

def simplify(var_idx):
    pass

def generate_random_instance(num_clauses, num_variables, k):
    assert num_variables >= k
    clause_categories = np.zeros(k+1)
    clause_categories[k] = num_clauses
    clauses, variables = [{} for _ in xrange(num_clauses)], [{} for _ in xrange(num_variables + 1)]
    max_num_conns = 0
    for clause_idx in xrange(num_clauses):
        clauses[clause_idx]["type"] = k
        clauses[clause_idx]["lits"] = k
        clauses[clause_idx]["literal"] = [{} for _ in xrange(k)]
        for curr_clause in xrange(k):
            while True:
                randvar = random.randint(1, num_variables)
                used = any(randvar == literal.get("var", -1) for literal in clauses[clause_idx]["literal"])
                if not used:
                    break
            clauses[clause_idx]["literal"][curr_clause]["var"] = randvar
            clauses[clause_idx]["literal"][curr_clause]["bar"] = random.randint(0, 1)
            if "clauses" not in variables[randvar]:
                variables[randvar]["clauses"] = 0
            variables[randvar]["clauses"] += 1
            if variables[randvar]["clauses"] > max_num_conns:
                max_num_conns = variables[randvar]["clauses"]
    for var_idx in xrange(1, num_variables+1):
        if variables[var_idx]["clauses"]:
            variables[var_idx]["clauselist"] = [{} for _ in xrange(variables[var_idx]["clauses"])]
            variables[var_idx]["clauses"] = 0
    for clause_idx in xrange(num_clauses):
        for curr_clause in xrange(k):
            #     var=clause[i].literal[j].var;
            curr_var_idx = clauses[clause_idx]["literal"][curr_clause]["var"]
            curr_var = variables[curr_var_idx]
            if "clause" not in curr_var["clauselist"][curr_var["clauses"]]:
                curr_var["clauselist"][curr_var["clauses"]]["clause"] = 0
            curr_var["clauselist"][curr_var["clauses"]]["clause"] += 1
            curr_var["clauselist"][curr_var["clauses"]]["lit"] = curr_clause
            curr_var["clauses"] += 1


    max_literals = k
    free_spin = num_variables
    return variables, clauses, max_num_conns, max_literals, free_spin

def randomize_eta():
    pass

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
    num_clauses, num_variables, k = 12, 3, 3
    variables, clauses, max_num_conns, max_literals, free_spin = generate_random_instance(num_clauses, num_variables, k)
    print variables
    print clauses
    print max_num_conns
