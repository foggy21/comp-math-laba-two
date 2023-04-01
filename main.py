from finite_differences import createFinDifTable
from numpy import linspace

# function x^2 + ln(x);
# [a; b] = [0,4; 0,9]
# x** = 0,42
# x*** = 0,87
# x**** = 0,67

a = 0.4
b = 0.9
nodes = 10
tableFinDif = []
x_stars =[0.42, 0.87, 0.67]
x_values = linspace(a, b, num=nodes)
header = ["n", "Aerror", "Rerror", "Terror"]
createFinDifTable(x_values, tableFinDif)
h = x_values[1] - x_values[0]
#print(tableFinDif)

for x_star in x_stars:
    t = (x_star - x_values[0]) / h
    print(t)