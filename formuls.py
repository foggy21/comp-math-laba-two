from math import factorial

def firstNewton(nodes, finDifTable, t):
    result = 0
    for i in range(len(nodes)):
        result += (finDifTable[i]/factorial(i+1)) * firstNewtonMultipy(i, t)
    return result

def firstNewtonMultipy(i, t):
    result = 1
    for j in range(i-1):
        result *= (t - j)
    return result

def secondNewton(nodes, finDifTable, t):
    result = 0
    for i in range(len(nodes)):
        result = finDifTable[i] * secondNewtonMultipy(i, t)
    return result

def secondNewtonMultipy(i, t):
    result = 1
    for j in range(1, i):
        result *= ((t + (j - 1))/j)
    return result

def firstGauss(nodes, finDifTable, t):
    result = 0
    for i in range(len(nodes)):
        result += (finDifTable[i] * (1/factorial(i+1))) * firstGaussMultipy(i, t)
    return result

def firstGaussMultipy(i, t):
    result = 1
    for j in range(i-1):
        if (j % 2 != 0):
            result *= (t - (j+1)/2)
        else:
            result *= (t + (j-1)/2)
    return result

def secondGauss(nodes, finDifTable, t):
    result = 0
    for i in range(len(nodes)):
        result += (finDifTable[i] * (1/factorial(i+1))) * secondGaussMultiply(i, t)
    return result

def secondGaussMultiply(i, t):
    result = 1
    for j in range(i-1):
        if (j % 2 != 0):
            result *= (t + (j+1)/2)
        else:
            result *= (t - (j+1)/2)
    return result