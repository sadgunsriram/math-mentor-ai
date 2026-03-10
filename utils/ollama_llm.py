import requests

def ask_llm(prompt):

    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)

        data = response.json()

        # Debug: print full response if needed
        print("OLLAMA RESPONSE:", data)

        return data.get("response", "LLM returned no response")

    except Exception as e:
        return f"Error contacting Ollama: {str(e)}"