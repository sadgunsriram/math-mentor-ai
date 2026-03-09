import json

def save_memory(entry):

    with open("memory.json", "a") as f:
        f.write(json.dumps(entry) + "\n")