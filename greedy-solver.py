import sys

lambda = 0.7
def main():
    query_file = open('query.txt')

    # Each line of the query file is a separate query
    for line in query_file:
        # First column is the variable names, second column is the query
        var, quer = line.split('\t')
        var = var.split(',')
        quer = quer.split(',')
        tables = {}
        for pred in quer:
            table = pred.split('(')[0]
            if table in tables:




if __name__== '__main__':
    sys.exit(main())
