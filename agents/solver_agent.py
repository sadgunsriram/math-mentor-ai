from sympy import symbols, solve
import re

def solve_problem(problem, context):

    try:

        # extract equation part
        equation = re.findall(r"(.*)=0", problem)

        if equation:
            expr = equation[0]

            # convert to sympy format
            expr = expr.replace("^", "**")
            expr = expr.replace(" ", "")

            x = symbols('x')

            result = solve(expr, x)

            return result

        return None

    except Exception as e:
        return None