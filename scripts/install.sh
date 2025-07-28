#!/bin/bash
# encoding: utf-8
# Copyright (c) 2024- SATURN
# AUTHORS
# Sukbong Kwon (Galois)

venv=venv

python -m venv ${venv}

# Activate python virtual environment
source ${venv}/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install torch
pip install torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt
echo "Done."
