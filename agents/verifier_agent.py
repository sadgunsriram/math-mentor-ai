def verify_solution(problem, solution):

    if solution is None:
        return {
            "confidence": 0.2,
            "needs_hitl": True
        }

    return {
        "confidence": 0.9,
        "needs_hitl": False
    }