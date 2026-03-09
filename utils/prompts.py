PARSER_PROMPT = """
You are a math parser.

Convert the following math question into structured JSON.

Question:
{question}

Return JSON format like:

{{
  "problem_text": "...",
  "topic": "algebra | calculus | probability | linear_algebra",
  "variables": [],
  "constraints": [],
  "needs_clarification": false
}}
"""