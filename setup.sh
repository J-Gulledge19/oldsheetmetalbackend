#!/usr/bin/env bash

# exit on error
set -o errexit

# Install dependencies
pip install -r dependencies.txt

# run migration
python manage.py migrate