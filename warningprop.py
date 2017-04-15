from read_cnf import read_cnf
import sys
import copy
import numpy as np
import numpy.random as npr

def initialize_warnings(clauses):
    """ warnings as buncha numpy arrs? """
    warnings = []
    for clause in clauses:
        warnings.append(npr.randint(2, size=len(clause)))
    return warnings

def check_convergence(new_warnings, warnings):
    for warning_idx, warning in enumerate(warnings):
        if not np.allclose(warning, new_warnings[warning_idx]):
            return False
    return True

def warning_update(clauses, variables, warnings):
    for warning_idx in xrange(len(warnings)):
        warnings[warning_idx] = npr.randint(2, size=len(warnings[warning_idx]))
    return warnings
##########################
##########################
##########################
##########################

def warning_propagation(clauses,
                        variables,
                        n_iters=2000):
    curr_warnings_1 = initialize_warnings(clauses)
    curr_warnings_2 = copy.deepcopy(curr_warnings_1)
    print "beginning warningprop..."
    for curr_iter in xrange(n_iters):
        if curr_iter % 100 == 0:
            print curr_iter, " / ", n_iters
        curr_warnings_1 = warning_update(clauses, variables, curr_warnings_1)
        if id(curr_warnings_1) == id(curr_warnings_2):
            print "============ ACK ============="
        if check_convergence(curr_warnings_1, curr_warnings_2):
            return curr_warnings_1
        # just exchange ref vars, to avoid copying too much
        temp = curr_warnings_1
        curr_warnings_1 = curr_warnings_2
        curr_warnings_2 = temp
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
