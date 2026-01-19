from .storage import load_tasks, save_tasks

def add_task(title: str) -> None:
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)

def list_tasks():
    return load_tasks()
