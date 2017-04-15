import sys

if __name__ == "__main__":
    assert len(sys.argv) == 2
    filename = sys.argv[1]
    with open(filename, "r") as cnf_file:
        lines = cnf_file.readlines()
        lines = [line for line in lines if line[0] != 'c']
        first_line, clause_lines = lines[0], lines[1:]
    _, _, num_vars, num_clauses = first_line.split()
    num_vars, num_clauses = int(num_vars), int(num_clauses)
    assert len(clause_lines) == num_clauses
    clauses = []
    for clause_line in clause_lines:
        nums = map(int, clause_line.split())
        # last member of nums is always 0
        clauses.append(nums[:-1])
    print clauses
