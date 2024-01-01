#!/bin/bash
pyenv local $PYTHON_VERSION
poetry env use $PYTHON_VERSION
poetry run pip install --upgrade pip
poetry install
poetry run pip list --format=freeze > requirements.txt
