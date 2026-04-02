#!/bin/bash

echo "Installing LogixCTF..."

if [ -d "temp_LogixCTF" ]; then
    echo "Removing existing temp_LogixCTF folder..."
    rm -rf temp_LogixCTF
fi

git clone https://github.com/ansamkhazaleh04/LogixCTF.git temp_LogixCTF
cd temp_LogixCTF || exit

chmod +x main.py

echo
echo "=============================="
echo "   LogixCTF Installation Done   "
echo "=============================="
echo

read -p "Do you want to run a demo on test.log? (y/n): " choice
if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
    echo "Running LogixCTF demo..."
    python3 main.py test.log
fi

echo
echo "Done! You can now run LogixCTF on any log file with:"
echo "python3 main.py <your_log_file>"