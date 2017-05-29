import sys
import copy
import numpy as np
import numpy.random as npr

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

def generate_random_instance(num_clauses, num_variables, k):
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
                randvar = random.randnint(1, N)
                # if(var==clause[i].literal[k].var) {
                used = any(randvar == var for var in some shit) #########
                if not used:
                    break
            clauses[clause_idx]["literal"][curr_clause]["var"] = randvar
            clauses[clause_idx]["literal"][curr_clause]["bar"] = randint(2)
            if not variables[randvar]["clauses"]:
                variables[randvar]["clauses"] = 0
            variables[randvar]["clauses"] += 1
            if variables[randvar]["clauses"] > max_num_conns:
                max_num_conns = variables[randvar]["clauses"]
    return variables, clauses, max_num_conns

if __name__ == "__main__":
    num_clauses, num_variables, k = 4200, 1000, 3
    generate_random_instance(num_clauses, num_variables, k)
