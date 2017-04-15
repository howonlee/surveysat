from read_cnf import read_cnf
import sys
import numpy as np
import numpy.random as npr

def initialize_warnings(clauses):
    """ warnings as buncha numpy arrs? """
    warnings = []
    for clause in clauses:
        warnings.append(npr.randint(2, size=len(clause)))
    return warnings

def check_convergence(warnings):
    pass

def warning_update(clauses, variables, warnings):
    pass

def warning_propagation(clauses,
                        variables,
                        n_iters=20000,
                        epsilon=0.001):
    warnings = initialize_warnings(clauses)
    for curr_iter in xrange(n_iters):
        warnings = warning_update(clauses, variables, warnings)
        if check_convergence(warnings):
            return warnings
    return False

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
    variables = clauses_to_variables(clauses, num_vars)
    warning_propagation(clauses, variables)
