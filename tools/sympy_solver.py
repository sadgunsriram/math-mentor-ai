from sympy import symbols, solve

def solve_equation(expr):

    x = symbols('x')

    try:
        result = solve(expr, x)
        return result

    except:
        return None