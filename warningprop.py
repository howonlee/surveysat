from read_cnf import read_cnf
import sys

if __name__ == "__main__":
    assert len(sys.argv) == 2
    filename = sys.argv[1]
    print read_cnf(filename)
