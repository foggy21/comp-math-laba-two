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
rnxes = []
debug_forumla = 0
#print(tableFinDif)

print("Значения иксов =", x_values)
x0 = 0

for x_star in x_stars:
    x_old = x_values[0]
    for x in x_values[1:]:
        if (x_old <= x_star and x_star <= x):
            if ((x_star - x_old) < (x - x_star)):
                x0 = x_old
            else:
                x0 = x
            break
        x_old = x
    print("x0 -", x0)
    cur_rnx = 0
    rnx_members.append(rnx(nodes, x0, x_values, x_star))
    t = (abs(x_star - x0)) / h
    if (x_star <= x_values[1]):
        cur_rnx = firstNewton(nodes, tableFinDif, t)
        debug_forumla = firstNewton
    if (x_star >= x_values[len(x_values)-2]):
        cur_rnx = secondNewton(nodes, tableFinDif, t)
        debug_forumla = secondNewton
    if (x_star > x_values[1] and x_star < x_values[int(len(x_values)/2)]):
        cur_rnx = firstGauss(nodes, tableFinDif, t)
        debug_forumla = firstGauss
    if (x_star < x_values[len(x_values)-2] and x_star > x_values[int(len(x_values)/2)]):
        cur_rnx = secondGauss(nodes, tableFinDif, t)
        debug_forumla = secondGauss
    
    cur_rnx -= func(x_star)
    print(debug_forumla.__str__())
    print("Rn(x) =",cur_rnx)
    rnxes.append(cur_rnx)

for cur_rnx in rnxes:
    print(min(rnx_members) < cur_rnx < max(rnx_members))

print(min(rnx_members))
print(max(rnx_members))
    #print(t)