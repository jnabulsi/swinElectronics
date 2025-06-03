import json
from pathlib import Path

def read_json(file_path: Path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def write_json(file_path: Path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

