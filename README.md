# Python Tasks Manager project

## Authors

Task Manager project was developed by GOUAULT Thibault in the context of a Python development project on github.

# Task Manager

Task Manager is a Python command-line application that helps users manage tasks with simple operations. The program allows the user to:

- **Add tasks**
- **Mark tasks as completed**
- **Remove tasks**
- **Display tasks**

It saves the task list in a JSON file for persistence across sessions.

---

## Features

- **Add Tasks**: Add a new task by entering its name.
- **List Tasks**: View the list of tasks, including their completion status.
- **Mark Tasks as Completed**: Mark a task as completed using its index in the list.
- **Remove Tasks**: Remove a task from the list using its index.
  
All tasks are stored in a JSON file (`tasks.json`), which is automatically loaded and saved whenever tasks are modified.

---

## Documentation

Documentation is available by opening the link : https://thibtob.github.io/SpaceDATAProject_GOUAULT_Thibault/ ,with any browser.

## Getting Started

Follow the steps below to set up and use the Task Manager on your local machine.

### Prerequisites

Ensure you have the following installed on your system:

1. **Python**: Version 3.12 or higher.
2. **PDM**: Python Dependency Manager. Install it via:
   ```bash
   pip install pdm


### Cloning the Repository

To get started, clone the repository from GitHub:
```bash
git clone https://github.com/thibtob/SpaceDATAProject_GOUAULT_Thibault.git
cd SpaceDATAProject_GOUAULT_Thibault

### Installing Dependencies
Install all required dependencies using pdm:
```bash
pdm install
```
This will create a virtual environment and install all necessary libraries listed in the pyproject.toml file.

### Using the Task Manager
To use the task manager, follow these steps:

1. Activate the virtual environment created by pdm:
```bash
pdm venv activate
```
If this doesn't work, manually activate the virtual environment:
```bash
source .venv/bin/activate  # For Linux/MacOS
.venv\Scripts\activate     # For Windows
```
2. Place yourself in the src/python_project_template folder using cd
3. Run the script using:
```bash
python dummy.py
```

