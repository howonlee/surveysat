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

def get_local_fields(warnings, num_vars):
    # sum of the warning for all adjacent clauses wrt a variable
    # ... is that correct?
    local_fields = []
    NotImplementedError() ###############

def get_contradiction_numbers(warnings):
    contradiction_numbers = []
    for warning in warnings:
        NotImplementedError() ###############
    return contradiction_numbers

def check_convergence(new_warnings, warnings):
    for warning_idx, warning in enumerate(warnings):
        if not np.allclose(warning, new_warnings[warning_idx]):
            return False
    return True

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


def warning_update(clauses, variables, warnings, num_warnings=40):
    """
    num_warnings is the number of warnings to impinge upon
    """
    cavity_fields = []
    for variable_idx, variable in enumerate(variables):
        curr_cavity_field = NotImplementedError()
        cavity_fields.append(curr_cavity_field)
    for warning_idx in xrange(len(warnings)):
        curr_warning = NotImplementedError()
        warnings[warning_idx] = curr_warning
    return warnings

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

def warning_decimation(clauses, variables):
    current_satisfying = {}
    for member in variables:
        warnings = warning_propagation(clauses, variables)
        if not warnings:
            return False
        local_fields = get_local_fields(warnings)
        contradiction_numbers = get_contradiction_numbers(warnings)
        if 1 in contradiction_numbers:
            return False
        ##################3
        ##################3
        ##################3
        ##################3
        new_clauses = NotImplementedError()
        new_variables = NotImplementedError()
        current_satisfying[NotImplemented] = NotImplementedError()
    return current_satisfying

if __name__ == "__main__":
    assert len(sys.argv) == 2
    clauses, num_vars, num_clauses = read_cnf(sys.argv[1])
    variables = clauses_to_variables(clauses, num_vars)
    warning_propagation(clauses, variables)
