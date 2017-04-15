import sys

if __name__ == "__main__":
    assert len(sys.argv) == 2
    filename = sys.argv[1]
    with open(filename, "r") as cnf_file:
        lines = cnf_file.readlines()
        init_line, clauses = lines[0], lines[1:]
    print init_line
    print "============="
    print "============="
    print "============="
    print clauses
