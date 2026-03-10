from utils.ollama_llm import ask_llm
from utils.prompts import PARSER_PROMPT

def parse_problem(text):

    prompt = PARSER_PROMPT.format(question=text)

    return ask_llm(prompt)