#!/bin/bash

# LogixCTF installer and runner

echo "Installing LogixCTF..."

# Create a temp folder
TMP_DIR=$(mktemp -d)
cd $TMP_DIR || exit

# Download files from GitHub
curl -sO https://raw.githubusercontent.com/ansamkhazaleh04/LogixCTF/main/main.py
curl -sO https://raw.githubusercontent.com/ansamkhazaleh04/LogixCTF/main/analyzer.py
curl -sO https://raw.githubusercontent.com/ansamkhazaleh04/LogixCTF/main/formatter.py
curl -sO https://raw.githubusercontent.com/ansamkhazaleh04/LogixCTF/main/test.log

# Make main.py executable
chmod +x main.py

echo "LogixCTF files downloaded."

# Run the tool
echo "Running LogixCTF..."
python3 main.py test.log