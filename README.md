LogixCTF: A Specialized Tool for Security Log Analysis

LogixCTF is a lightweight command-line tool designed to analyze log files, detect suspicious activities, and provide "meaningful hints for security learners, SOC analysts, and CTF players."
Quick Install & Run

For users who want a "fast setup without manual installation," you can deploy the tool using the following command:

curl -s https://raw.githubusercontent.com/ansamkhazaleh04/LogixCTF/main/install.sh | bash

This automated script will:

    "Download all required project files"

    "Prepare the tool for execution"

    "Allow you to run LogixCTF on any log file"

System Requirements

    Python 3.10 or newer

    Terminal (Linux / macOS / Windows)

Manual Installation

Alternatively, the repository can be set up manually:

git clone https://github.com/ansamkhazaleh04/LogixCTF.git
cd LogixCTF
Usage

To analyze any log file, use the following commands:

    Linux / macOS: python3 main.py <your_log_file>

    Windows: python main.py <your_log_file>

Users should "replace <your_log_file> with the path to your log file" to begin the investigation.
Project Structure

The project is organized into these primary components:

    "main.py" – The "entry point of the tool."

    "analyzer.py" – Contains the "core logic for detecting suspicious behavior."

    "formatter.py" – "Formats and displays results" for the user.

    "install.sh" – The "automated installer" script.

    "README.md" – Official "project documentation."

How It Works

LogixCTF follows a simple, effective workflow:

    Reads the provided log file.

    Analyzes specific patterns such as "repeated failed logins" and "suspicious IP behavior."

    Outputs clear "alerts" and "helpful hints" for the user.

Purpose and Educational Value

This tool is specifically "built for CTF players, SOC analyst trainees, and cybersecurity learners." It serves as a practical resource to help users understand how to "analyze logs," "detect attack patterns," and "think like a security analyst."
Notes

    LogixCTF is an "educational tool, not a full SIEM system."

    It "works best with structured log files."

    The framework "can be extended to detect more attack patterns" as needed.

Author: Ansam Alkhazaleh