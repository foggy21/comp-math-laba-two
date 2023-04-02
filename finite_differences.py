from function import func

def createFinDifTable(x):
    n = len(x)
    table = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        table[i][0] = func(x[i])
    for i in range(1, n):
        for j in range(n-i):
            table[i][j] = (table[i][j] - table[i-1][j])
    return table
