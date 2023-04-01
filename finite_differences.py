from function import func

def createFinDifTable(x_values, table = []):
    if (len(x_values) == 2):
        fin_dif = func(x_values[1]) - func(x_values[0])
        table.append(fin_dif)
        return fin_dif
    if (len(x_values) > 2):
        fin_dif = createFinDifTable(x_values[1:len(x_values)-1], table) - createFinDifTable(x_values[0:len(x_values)-2], table)
        table.append(fin_dif)
        return fin_dif

