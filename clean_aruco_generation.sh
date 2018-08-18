#!/bin/sh
virtualenv .venv_clean --python=python3
. ./.venv_clean/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

python ./scripts/marker_file_generator.py

rm -rf ./.venv_clean