from math import log
def func(x):
    return x**2 + log(x)

def der_func(x):
    return 2*x + 1/x