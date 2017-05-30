import sys
import copy
import numpy as np
import numpy.random as npr
import random

"""
sort of a port of the mezard et al collab's c implementation
nontrivial changes, tho
"""

def fix(var_idx, spin):
    pass

def simplify(var_idx):
    pass

def incr(parent, key):
    """ mutates """
    if key not in parent:
        parent[key] = 0
    parent[key] += 1

def generate_random_instance(num_clauses, num_variables, k):
    assert num_variables >= k
    clause_categories = [0 for _ in xrange(k+1)]
    clause_categories[k] = num_clauses
    clauses, variables = [{} for _ in xrange(num_clauses)], [{} for _ in xrange(num_variables + 1)]
    max_num_conns = 0
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
            incr(variables[randvar], "clauses")
            if variables[randvar]["clauses"] > max_num_conns:
                max_num_conns = variables[randvar]["clauses"]
    """ count up var datastruct """
    for var_idx in xrange(1, num_variables+1):
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
    num_clauses, num_variables, k = 3, 3, 3
    variables, clauses, max_num_conns, max_literals, free_spin = generate_random_instance(num_clauses, num_variables, k)
    print variables
    print clauses
    print max_num_conns
