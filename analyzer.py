from collections import defaultdict
from formatter import info, warning, hint, section, success

FAILED_THRESHOLD = 3

def parse_line(line):
    parts = line.split()
    if len(parts) < 1:
        return None
    
    return {
        "ip": parts[0],
        "raw": line
    }

def analyze_failed_logins(lines):
    failed = defaultdict(int)

    for line in lines:
        if "401" in line:
            data = parse_line(line)
            if data:
                failed[data["ip"]] += 1

    return failed

def analyze_log(file_path):
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()

        info(f"Loaded file: {file_path}")
        info(f"Total log entries: {len(lines)}")

        section("Analysis: Failed Logins")

        failed_logins = analyze_failed_logins(lines)
        suspicious_found = False

        for ip, count in failed_logins.items():
            if count >= FAILED_THRESHOLD:
                warning(f"{ip} → {count} failed login attempts")
                suspicious_found = True

        if not suspicious_found:
            success("No suspicious failed login patterns detected")

        section("Hints")

        if suspicious_found:
            hint("Multiple failed logins may indicate brute-force attempts.")
            hint("Focus on repeated IP behavior.")
        else:
            hint("Try analyzing request patterns or timing anomalies.")

    except FileNotFoundError:
        warning("Log file not found!")