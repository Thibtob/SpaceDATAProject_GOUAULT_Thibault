# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(
    0,
    os.path.abspath(
        "C:/Users/utilisateur/Documents/COURS 5A ESPACE/COURS 5A/TRONC COMMUN/Space DATA\projet Github/python_project_template-main/src"
    ),
)


project = "GitHubProjectSpaceData"
copyright = "2024, GOUAULT Thibault"
author = "GOUAULT Thibault"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


# Ajouter l'extension sphinx.ext.autodoc
extensions = ["sphinx.ext.autodoc"]  # Génère la documentation à partir des docstrings


templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
