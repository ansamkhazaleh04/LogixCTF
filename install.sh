#!/bin/bash

echo "Installing LogixCTF..."

rm -rf temp_LogixCTF

git clone https://github.com/ansamkhazaleh04/LogixCTF.git temp_LogixCTF
cd temp_LogixCTF || exit

chmod +x main.py

echo
echo "=============================="
echo "   LogixCTF Installation Done   "
echo "=============================="
echo

echo "Running LogixCTF demo on test.log..."
python3 main.py test.log

echo
echo "Done! You can now run LogixCTF on any log file with:"
echo "python3 main.py <your_log_file>"