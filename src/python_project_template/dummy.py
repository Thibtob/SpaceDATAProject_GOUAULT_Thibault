"""
Task management module.

This module provides functionality to add, list, mark as completed,
and delete tasks, with storage in a JSON file.
"""

import json
import os

# Path to the file where tasks are stored
TASKS_FILE = "tasks.json"


def load_tasks():
    """
    Load tasks from the JSON file.

    Returns:
        list: A list of tasks, where each task is a dictionary with the keys
        'name' (str) and 'completed' (bool).
    """
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    else:
        return []


def save_tasks(tasks):
    """
    Save tasks to a JSON file.

    Args:
        tasks (list): A list of tasks to save.
    """
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, task_name):
    """
    Add a new task.

    Args:
        tasks (list): The current list of tasks.
        task_name (str): The name of the task to add.

    Effects:
        Adds a new task to the list and saves it.
    """
    task = {"name": task_name, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task_name}' added.")


def list_tasks(tasks):
    """
    Display tasks.

    Args:
        tasks (list): The current list of tasks.

    Effects:
        Prints each task with its status (completed or not) to the console.
    """
    if len(tasks) == 0:
        print("No tasks to display.")
    else:
        print("\nTask List:")
        for index, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Not completed"
            print(f"{index}. {task['name']} - {status}")


def complete_task(tasks, task_index):
    """
    Mark a task as completed.

    Args:
        tasks (list): The current list of tasks.
        task_index (int): The index of the task to mark as completed (1-based).

    Effects:
        Updates the selected task's status to completed and saves the list.

    Raises:
        IndexError: If the index is out of bounds.
    """
    if task_index > 0 and task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        save_tasks(tasks)
        print(f"Task {task_index} marked as completed.")
    else:
        print("Invalid task number.")


def remove_task(tasks, task_index):
    """
    Remove a task.

    Args:
        tasks (list): The current list of tasks.
        task_index (int): The index of the task to remove (1-based).

    Effects:
        Deletes the selected task from the list and saves it.

    Raises:
        IndexError: If the index is out of bounds.
    """
    if task_index > 0 and task_index <= len(tasks):
        task_name = tasks.pop(task_index - 1)["name"]
        save_tasks(tasks)
        print(f"Task '{task_name}' removed.")
    else:
        print("Invalid task number.")


def main():
    """
    Main entry point of the program.

    Displays an interactive menu to manage tasks, with options to add,
    list, mark as completed, or remove tasks.
    """
    tasks = load_tasks()

    while True:
        print("\n--- Task Management Menu ---")
        print("1. Add a task")
        print("2. List tasks")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            task_name = input("Enter the name of the task: ")
            add_task(tasks, task_name)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            task_index = int(
                input("Enter the number of the task to mark as completed: ")
            )
            complete_task(tasks, task_index)
        elif choice == "4":
            task_index = int(input("Enter the number of the task to remove: "))
            remove_task(tasks, task_index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
