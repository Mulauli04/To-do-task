import json
from datetime import datetime, timedelta

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or JSON decoding fails, initialize an empty list
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        # Save tasks to "tasks.json" with an indentation of 2 spaces
        json.dump(tasks, file, indent=2)

def display_tasks(tasks):
    if tasks:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            # Display task details with index, description, priority, category, and due date
            print(f"{index}. {task['description']} - Priority: {task['priority']} - Category: {task['category']} - Due: {task['due_date']}")
    else:
        print("Your to-do list is empty.")

def add_task(tasks, description, priority, category, due_date):
    new_task = {
        "description": description,
        "priority": priority,
        "category": category,
        "due_date": due_date
    }
    # Add the new task to the tasks list and save
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")

def remove_task(tasks, task_index):
    try:
        # Remove the task at the specified index and save
        removed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Removed task: {removed_task['description']}")
    except IndexError:
        print("Invalid task index. No task removed.")

def edit_task(tasks, task_index, new_description, new_priority, new_category, new_due_date):
    try:
        # Access the task at the specified index and update details
        task = tasks[task_index - 1]
        task['description'] = new_description
        task['priority'] = new_priority
        task['category'] = new_category
        task['due_date'] = new_due_date
        save_tasks(tasks)
        print("Task edited successfully!")
    except IndexError:
        print("Invalid task index. No task edited.")

def due_date_reminder(tasks):
    today = datetime.now().date()
    # Filter tasks with due dates within the next three days
    upcoming_tasks = [task for task in tasks if task["due_date"] and datetime.strptime(task["due_date"], "%Y-%m-%d").date() <= today + timedelta(days=3)]

    if upcoming_tasks:
        print("\nUpcoming Due Dates:")
        for task in upcoming_tasks:
            # Display tasks with upcoming due dates
            print(f"{task['description']} - Due: {task['due_date']}")
    else:
        print("\nNo upcoming due dates.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Display tasks\n2. Add task\n3. Remove task\n4. Edit task\n5. Due Date Reminder\n6. Quit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            description = input("Enter task description: ")
            priority = input("Enter task priority (Low/Medium/High): ")
            category = input("Enter task category: ")
            due_date = input("Enter due date (YYYY-MM-DD, leave blank if none): ")
            add_task(tasks, description, priority, category, due_date)
        elif choice == "3":
            display_tasks(tasks)
            task_index = int(input("Enter the index of the task to remove: "))
            remove_task(tasks, task_index)
        elif choice == "4":
            display_tasks(tasks)
            task_index = int(input("Enter the index of the task to edit: "))
            new_description = input("Enter new task description: ")
            new_priority = input("Enter new task priority (Low/Medium/High): ")
            new_category = input("Enter new task category: ")
            new_due_date = input("Enter new due date (YYYY-MM-DD, leave blank to keep the current date): ")
            edit_task(tasks, task_index, new_description, new_priority, new_category, new_due_date)
        elif choice == "5":
            due_date_reminder(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
main()