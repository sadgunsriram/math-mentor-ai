from utils.gemini_llm import ask_gemini

def explain_solution(problem, solution):

    prompt = f"""
Explain step-by-step solution.

Problem:
{problem}

Answer:
{solution}
"""

    return ask_gemini(prompt)