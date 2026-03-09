def route_problem(parsed_problem):

    topic = parsed_problem.get("topic")

    if topic == "algebra":
        return "algebra_solver"

    if topic == "probability":
        return "probability_solver"

    if topic == "calculus":
        return "calculus_solver"

    return "general_solver"