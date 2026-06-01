import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


# Load tasks from JSON file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save tasks to JSON file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Add new task
def add_task(tasks):
    title = input("Enter task title: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (High/Medium/Low): ").capitalize()

    task = {
        "title": title,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")


# View pending tasks sorted by due date
def view_tasks(tasks):
    pending_tasks = [task for task in tasks if not task["completed"]]

    pending_tasks.sort(key=lambda x: x["due_date"])

    if not pending_tasks:
        print("No pending tasks.\n")
        return

    print("\nPending Tasks:")
    for i, task in enumerate(pending_tasks, start=1):
        print(f"{i}. {task['title']} | Due: {task['due_date']} | Priority: {task['priority']}")
    print()


# Mark task as completed
def mark_completed(tasks):
    view_tasks(tasks)

    try:
        index = int(input("Enter task number to mark completed: ")) - 1

        pending_tasks = [task for task in tasks if not task["completed"]]

        if 0 <= index < len(pending_tasks):
            pending_tasks[index]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!\n")
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


# Delete task
def delete_task(tasks):
    if not tasks:
        print("No tasks available.\n")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} ({status})")

    try:
        index = int(input("Enter task number to delete: ")) - 1

        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted task: {removed['title']}\n")
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


# Show overdue tasks
def show_overdue_tasks(tasks):
    today = datetime.today().date()

    overdue = [
        task for task in tasks
        if not task["completed"] and
        datetime.strptime(task["due_date"], "%Y-%m-%d").date() < today
    ]

    if overdue:
        print("\n*** OVERDUE TASKS ***")
        for task in overdue:
            print(f"- {task['title']} (Due: {task['due_date']})")
        print()


# Filter by priority
def filter_by_priority(tasks):
    priority = input("Enter priority (High/Medium/Low): ").capitalize()

    filtered = [
        task for task in tasks
        if task["priority"] == priority and not task["completed"]
    ]

    if not filtered:
        print("No matching tasks found.\n")
        return

    print(f"\n{priority} Priority Tasks:")
    for i, task in enumerate(filtered, start=1):
        print(f"{i}. {task['title']} | Due: {task['due_date']}")
    print()


# Main menu
def main():
    tasks = load_tasks()

    show_overdue_tasks(tasks)

    while True:
        print("===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. View Pending Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Filter by Priority")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            mark_completed(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            filter_by_priority(tasks)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
