from utils.ollama_llm import ask_llm

def explain_solution(problem, solution):

    prompt = f"""
Explain the following math solution step-by-step.

Problem:
{problem}

Answer:
{solution}

Explain clearly so that a student can understand.
"""

    return ask_llm(prompt)