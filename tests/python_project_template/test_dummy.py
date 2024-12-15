"""Testing dummy file."""

from python_project_template.dummy import dummy
from unittest import mock
import unittest
import pytest
from unittest.mock import patch, mock_open
from python_project_template.dummy import (
    add_task,
    list_tasks,
    complete_task,
    remove_task,
    load_tasks,
    save_tasks,
    main,
)

TASKS_FILE = "tasks.json"


def test_dummy() -> None:
    """Dummy test"""
    assert dummy() == "dummy"


# Mock de la fonction load_tasks pour ne pas avoir à lire de fichier
@pytest.fixture
def mock_tasks():
    return [
        {"name": "Task 1", "completed": False},
        {"name": "Task 2", "completed": True},
    ]


# Test de add_task
@patch("python_project_template.dummy.save_tasks")
def test_add_task(mock_save, mock_tasks):
    tasks = mock_tasks
    add_task(tasks, "New Task")

    # Vérifier si la tâche a été ajoutée
    assert len(tasks) == 3
    assert tasks[-1]["name"] == "New Task"

    # Vérifier si save_tasks a été appelé
    mock_save.assert_called_once_with(tasks)


# Test de list_tasks
@patch("builtins.print")
def test_list_tasks(mock_print, mock_tasks):
    list_tasks(mock_tasks)

    # Vérifier si les tâches ont été imprimées correctement
    mock_print.assert_any_call("1. Task 1 - Not completed")
    mock_print.assert_any_call("2. Task 2 - Completed")


# Test de complete_task
@patch("python_project_template.dummy.save_tasks")
def test_complete_task(mock_save, mock_tasks):
    tasks = mock_tasks
    complete_task(tasks, 1)

    # Vérifier si la tâche est marquée comme terminée
    assert tasks[0]["completed"] is True

    # Vérifier si save_tasks a été appelé
    mock_save.assert_called_once_with(tasks)


# Test de remove_task
@patch("python_project_template.dummy.save_tasks")
def test_remove_task(mock_save, mock_tasks):
    tasks = mock_tasks
    remove_task(tasks, 1)

    # Vérifier si la tâche a été supprimée
    assert len(tasks) == 1
    assert tasks[0]["name"] == "Task 2"

    # Vérifier si save_tasks a été appelé
    mock_save.assert_called_once_with(tasks)


# Test de load_tasks
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"name": "Task 1", "completed": false}]',
)
def test_load_tasks(mock_file):
    tasks = load_tasks()

    # Vérifier que le fichier est bien ouvert
    mock_file.assert_called_once_with("tasks.json", "r")

    # Vérifier que les tâches sont correctement chargées
    assert len(tasks) == 1
    assert tasks[0]["name"] == "Task 1"


# Test d'IndexError dans complete_task
@patch("python_project_template.dummy.save_tasks")
def test_complete_task_index_error(mock_save, mock_tasks):
    tasks = mock_tasks
    # Tester un index hors de portée
    complete_task(tasks, 999)

    # Vérifier que l'état de la tâche n'a pas changé
    assert tasks[0]["completed"] is False
    assert tasks[1]["completed"] is True


# Test d'IndexError dans remove_task
@patch("python_project_template.dummy.save_tasks")
def test_remove_task_index_error(mock_save, mock_tasks):
    tasks = mock_tasks
    # Tester un index hors de portée
    remove_task(tasks, 999)

    # Vérifier que la liste n'a pas changé
    assert len(tasks) == 2


# Test de load_tasks avec un fichier inexistant
@patch("builtins.open", new_callable=mock_open, read_data="[]")
def test_load_tasks_empty(mock_file):
    tasks = load_tasks()

    # Vérifier que le fichier est bien ouvert
    mock_file.assert_called_once_with("tasks.json", "r")

    # Vérifier que les tâches sont vides
    assert tasks == []


# Test de load_tasks avec une erreur de fichier (FileNotFoundError)
@patch("builtins.open", side_effect=FileNotFoundError)
def test_load_tasks_file_not_found(mock_file):
    with pytest.raises(FileNotFoundError):
        load_tasks()


# Test de la gestion des erreurs de load_tasks (fichier valide)
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"name": "Task 1", "completed": false}]',
)
def test_load_tasks_valid(mock_file):
    tasks = load_tasks()

    # Vérifier que les tâches sont chargées correctement
    assert len(tasks) == 1
    assert tasks[0]["name"] == "Task 1"


# Test de la gestion des tâches marquées comme terminées
def test_mark_task_as_completed(mock_tasks):
    tasks = mock_tasks
    complete_task(tasks, 1)

    # Vérifier que la tâche est marquée comme terminée
    assert tasks[0]["completed"] is True


# Test de complete_task avec une tâche déjà terminée
@patch("python_project_template.dummy.save_tasks")
def test_complete_task_already_completed(mock_save, mock_tasks):
    tasks = mock_tasks
    tasks[0]["completed"] = True  # Marquer la tâche comme déjà terminée

    # Appeler complete_task sur la tâche déjà terminée
    complete_task(tasks, 0)

    # Vérifier que la tâche ne change pas
    assert tasks[0]["completed"] is True
    mock_save.assert_not_called()  # Pas besoin de sauvegarder si aucune modification


# Test de load_tasks avec un fichier valide
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"name": "Task 1", "completed": false}]',
)


# Test de save_tasks
@patch("builtins.open", new_callable=mock_open)
@patch("json.dump")
def test_save_tasks(mock_json_dump, mock_file):
    # Exemple de tâches
    mock_tasks = [
        {"name": "Task 1", "completed": False},
        {"name": "Task 2", "completed": True},
    ]

    # Appel de la fonction save_tasks
    save_tasks(mock_tasks)

    # Vérifier que le fichier est bien ouvert en mode écriture
    mock_file.assert_called_once_with(TASKS_FILE, "w")

    # Vérifier que json.dump a été appelé avec les bonnes données et le bon fichier
    mock_json_dump.assert_called_once_with(mock_tasks, mock_file(), indent=4)


# Test de main (avec un scénario complet)
class TestTaskManagement(unittest.TestCase):
    @mock.patch("python_project_template.dummy.save_tasks")
    @mock.patch("python_project_template.dummy.load_tasks")
    @mock.patch("builtins.print")
    @mock.patch(
        "builtins.input", side_effect=["1", "New Task", "5"]
    )  # Simule l'entrée utilisateur
    def test_main(self, mock_input, mock_print, mock_load, mock_save):
        # Liste initiale des tâches simulée
        initial_tasks = [
            {"name": "Task 1", "completed": False},
            {"name": "Task 2", "completed": True},
        ]
        mock_load.return_value = initial_tasks  # Simule le chargement des tâches

        # Appel de la fonction main
        main()

        # Vérifie si la fonction add_task a bien été appelée avec la bonne liste de tâches et le bon nom de tâche
        mock_save.assert_called_once()  # Vérifie que save_tasks a bien été appelée au moins une fois

        # Vérifie que save_tasks a bien été appelée avec la liste mise à jour
        new_task_list = [
            {"name": "Task 1", "completed": False},
            {"name": "Task 2", "completed": True},
            {"name": "New Task", "completed": False},  # Nouvelle tâche ajoutée
        ]

        # Vérifie que save_tasks a bien été appelée avec la liste mise à jour
        mock_save.assert_called_with(new_task_list)

        # Vérifie que print affiche les tâches mises à jour
        mock_print.assert_any_call("Task 'New Task' added.")
        mock_print.assert_any_call("1. Task 1 - Not completed")
        mock_print.assert_any_call("2. Task 2 - Completed")
        mock_print.assert_any_call("3. New Task - Not completed")

        # Vérifie que input a bien été appelé pour obtenir les entrées de l'utilisateur
        mock_input.assert_any_call("Choose an option (1-5): ")
        mock_input.assert_any_call("Enter the name of the task: ")


if __name__ == "__main__":
    unittest.main()
