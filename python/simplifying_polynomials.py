import re

def simplify(poly):
    matches = re.findall(r'([+\-]?)(\d*)([a-z]+)', poly)
    expression = [[int(i[0] + (i[1] if i[1] != "" else "1")), ''.join(sorted(i[2]))] for i in matches]
    variables = sorted(list(set(i[1] for i in expression)), key=lambda x: (len(x), x))
    coefficients = {v:sum(i[0] for i in expression if i[1] == v) for v in variables}

    return '+'.join(str(coefficients[v]) + v for v in variables if coefficients[v] != 0).replace('1','').replace('+-','-')
