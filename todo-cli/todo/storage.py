import json
import os

DATA_PATH = os.path.join("data", "tasks.json")

def load_tasks():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DATA_PATH):
        return []
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    os.makedirs("data", exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)
