from utils.gemini_llm import ask_gemini
from utils.prompts import PARSER_PROMPT

def parse_problem(text):

    prompt = PARSER_PROMPT.format(question=text)

    return ask_gemini(prompt)