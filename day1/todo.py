import json
import os

TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Add new task
def add_task(task):
    tasks.append({"task": task, "completed": False})
    save_tasks()
    print("Task added!")

# List all tasks
def list_tasks():
    if not tasks:
        print("\nNo tasks yet!")
        return
    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['task']}")
    print()

# Mark task complete
def mark_completed(index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["completed"] = True
        save_tasks()
        print("Task marked as complete!")
    else:
        print("Invalid task index!")

# Load existing tasks at start
tasks = load_tasks()

# Main loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Mark as complete")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)

    elif choice == "2":
        list_tasks()

    elif choice == "3":
        list_tasks()
        try:
            index = int(input("Enter the task number: "))
            mark_completed(index)
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1, 2, 3 or 4.")
