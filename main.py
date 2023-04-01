from finite_differences import createFinDifTable
from function import func
from formulas import firstNewton, secondNewton, firstGauss, secondGauss, rnx
from numpy import linspace

# function x^2 + ln(x);
# [a; b] = [0,4; 0,9]
# x** = 0,42
# x*** = 0,87
# x**** = 0,67

a = 0.4
b = 0.9
nodes = 10

x_stars =[0.42, 0.87, 0.67]
x_values = linspace(a, b, num=nodes)
header = ["n", "Aerror", "Rerror", "Terror"]
tableFinDif = createFinDifTable(x_values)
h = x_values[1] - x_values[0]
rnx_members = []
#print(tableFinDif)

for x_star in x_stars:
    rnx_members.append(rnx(nodes, x_values, x_star))

print(min(rnx_members))
print(max(rnx_members))

for x_star in x_stars:
    cur_rnx = 0
    t = (x_star - x_values[0]) / h
    if (x_star <= x_values[1]):
        cur_rnx = firstNewton(nodes, tableFinDif, t)
    if (x_star >= x_values[len(x_values)-2]):
        cur_rnx = secondNewton(nodes, tableFinDif, t)
    if (x_star > x_values[1] and x_star < x_values[int(len(x_values)/2)]):
        cur_rnx = firstGauss(nodes, tableFinDif, t)
    if (x_star < x_values[len(x_values)-2] and x_star > x_values[int(len(x_values)/2)]):
        cur_rnx = secondGauss(nodes, tableFinDif, t)
    
    cur_rnx -= func(x_star)
    print(min(rnx_members) < cur_rnx < max(rnx_members))

    #print(t)