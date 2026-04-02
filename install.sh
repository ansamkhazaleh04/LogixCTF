#!/bin/bash
# LogixCTF Installer & Demo Script

echo "Installing LogixCTF..."
git clone https://github.com/ansamkhazaleh04/LogixCTF.git temp_LogixCTF
cd temp_LogixCTF || exit

# Make main.py executable
chmod +x main.py

echo
echo "=============================="
echo "   LogixCTF Installation Done   "
echo "=============================="
echo

# Ask user if they want to run demo
read -p "Do you want to run a demo on test.log? (y/n): " choice
if [[ "$choice" == "y" || "$choice" == "Y" ]]; then
    echo "Running LogixCTF demo..."
    python3 main.py test.log
else
    echo "Skipping demo."
fi

echo
echo "Done! You can now run LogixCTF on any log file with:"
echo "python3 main.py <your_log_file>"