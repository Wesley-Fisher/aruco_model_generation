#!/bin/sh
virtualenv .venv --python=python3
. ./.venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt