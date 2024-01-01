#!/bin/bash
pyenv install $PYTHON_VERSION
poetry config virtualenvs.path ./.venv --local
poetry init --no-interaction \
    --name $PACKAGE_NAME \
    --author $PACKAGE_AUTHOR \
    --description $PACKAGE_DESCRIPTION \
    --license $PACKAGE_LICENSE \
    --python $PYTHON_VERSION
