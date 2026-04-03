LogixCTF - Security Log Analysis Tool for SOC & CTF Training

LogixCTF is a lightweight command-line tool designed to analyze log files, detect suspicious activities, and provide meaningful hints for security learners, SOC analysts, and CTF players.
Quick Install & Run

For users who want a fast setup without manual installation:
Bash

curl -s https://raw.githubusercontent.com/ansamkhazaleh04/LogixCTF/main/install.sh | bash

This script will:

    Download all required project files

    Prepare the tool for execution

    Allow you to run LogixCTF on any log file

System Requirements

    Python 3.10 or newer

    Terminal (Linux / macOS / Windows)

Manual Installation
Bash

git clone https://github.com/ansamkhazaleh04/LogixCTF.git
cd LogixCTF

Usage

To analyze any log file:

Linux / macOS:
Bash

python3 main.py <your_log_file>

Windows:
Bash

python main.py <your_log_file>

    Replace <your_log_file> with the path to your log file.

Project Structure

    main.py – Entry point of the tool

    analyzer.py – Core logic for detecting suspicious behavior

    formatter.py – Formats and displays results

    install.sh – Automated installer

    README.md – Project documentation

How It Works

LogixCTF follows a simple workflow:

    Reads the provided log file

    Analyzes patterns such as:

        Repeated failed logins

        Suspicious IP behavior

    Outputs:

        Alerts

        Helpful hints

Purpose

This tool is built for:

    CTF players

    SOC analyst trainees

    Cybersecurity learners

It helps users understand how to analyze logs, detect attack patterns, and think like a security analyst.
Notes

    LogixCTF is an educational tool, not a full SIEM system

    Works best with structured log files

    Can be extended to detect more attack patterns

Author: Ansam Alkhazaleh 