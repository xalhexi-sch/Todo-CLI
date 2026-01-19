from todo.core import add_task, list_tasks

def menu():
    print("\n=== TODO CLI ===")
    print("1) Add task")
    print("2) List tasks")
    print("0) Exit")

def main():
    while True:
        menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            title = input("Task title: ").strip()
            if not title:
                print("Title cannot be empty.")
                continue
            add_task(title)
            print("Task added!")

        elif choice == "2":
            tasks = list_tasks()
            if not tasks:
                print("No tasks yet.")
            else:
                print("\nYour tasks:")
                for i, t in enumerate(tasks, start=1):
                    status = "✓" if t.get("done") else " "
                    print(f"{i}. [{status}] {t['title']}")

        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
