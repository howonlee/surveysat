from read_cnf import read_cnf
import sys

def warning_update():
    pass

def warning_propagation(clauses, n_iters=20000):
    pass

def clauses_to_variables(clauses, num_vars):
    variables = [[] for _ in xrange(num_vars)]
    return variables

if __name__ == "__main__":
    assert len(sys.argv) == 2
    clauses, num_vars, num_clauses = read_cnf(sys.argv[1])
    warning_propagation(clauses)
