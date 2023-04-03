from function import func

def createFinDifTable(x):
    n = len(x)
    table = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        table[i][0] = func(x[i])
    for j in range(1, n):
        for i in range(n-j):
            table[i][j] = (table[i][j-1] - table[i-1][j-1])
    return table
