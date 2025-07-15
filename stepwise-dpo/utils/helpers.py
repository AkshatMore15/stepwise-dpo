import json

def load_jsonl(path: str) -> list:
    """Load a .jsonl file and return a list of dicts."""
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]