from read_cnf import read_cnf
import sys
import random

def initialize_warnings(clauses):
    pass

def warning_update(clauses, variables, warnings):
    pass

def warning_propagation(clauses,
                        variables,
                        n_iters=20000,
                        epsilon=0.001):
    for curr_iter in xrange(n_iters):
        pass

def clauses_to_variables(clauses, num_vars):
    # 0 will be empty
    variables = [[] for _ in xrange(num_vars+1)]
    for clause_idx, clause in enumerate(clauses):
        for member in clause:
            if member > 0:
                variables[member].append(clause_idx)
            else:
                variables[-member].append(-clause_idx)
    return variables

if __name__ == "__main__":
    assert len(sys.argv) == 2
    clauses, num_vars, num_clauses = read_cnf(sys.argv[1])
    clauses_to_variables(clauses, num_vars)
    # warning_propagation(clauses)
