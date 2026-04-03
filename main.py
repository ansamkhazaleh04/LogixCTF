from collections import defaultdict
from formatter import info, warning, hint, section, success
import os
import subprocess

FAILED_THRESHOLD = 3

def parse_line(line):
    data = {"raw": line, "type": None, "ip": "unknown", "user": "unknown", "status": None}
    if "LOGIN" in line or "Failed password" in line:
        data["type"] = "login"
        data["status"] = "FAILED" if "Failed" in line else "SUCCESS"
        parts = line.split()
        for part in parts:
            if part.startswith("user=") or "for" in part:
                data["user"] = part.split("=")[-1]
            if part.count('.') == 3:
                data["ip"] = part
    elif "sudo" in line or "root" in line:
        data["type"] = "privilege"
        for part in line.split():
            if part.startswith("user="):
                data["user"] = part.split("=")[1]
    elif "modified" in line or "changed" in line or "/etc" in line:
        data["type"] = "file"
    elif "connection refused" in line or "unauthorized" in line or "denied" in line:
        data["type"] = "network"
        for part in line.split():
            if part.count('.') == 3:
                data["ip"] = part
    return data

def analyze_failed_logins(lines):
    failed = defaultdict(int)
    for line in lines:
        data = parse_line(line)
        if data and data["type"] == "login" and data["status"] == "FAILED":
            failed[data["ip"]] += 1
    return failed

def analyze_privilege_changes(lines):
    alerts = []
    for line in lines:
        data = parse_line(line)
        if data and data["type"] == "privilege":
            alerts.append(f"Privilege escalation detected for user {data['user']}")
    return alerts

def analyze_file_changes(lines):
    alerts = []
    for line in lines:
        data = parse_line(line)
        if data and data["type"] == "file":
            alerts.append(f"Sensitive file change detected: {data['raw'].strip()}")
    return alerts

def analyze_network_issues(lines):
    alerts = []
    for line in lines:
        data = parse_line(line)
        if data and data["type"] == "network":
            alerts.append(f"Network issue detected from IP {data['ip']}: {data['raw'].strip()}")
    return alerts

def load_logs():
    logs = []
    auth_paths = ["/var/log/auth.log", "/var/log/secure"]
    for path in auth_paths:
        if os.path.exists(path):
            with open(path, "r") as f:
                logs += f.readlines()
    try:
        sudo_logs = subprocess.check_output(["journalctl", "_COMM=sudo", "-n", "1000"], text=True)
        logs += sudo_logs.splitlines()
    except Exception:
        pass
    try:
        file_logs = subprocess.check_output(["journalctl", "-n", "1000"], text=True)
        for line in file_logs.splitlines():
            if "/etc" in line and ("modified" in line or "changed" in line):
                logs.append(line)
    except Exception:
        pass
    try:
        network_logs = subprocess.check_output(["journalctl", "-n", "1000"], text=True)
        for line in network_logs.splitlines():
            if any(x in line for x in ["connection refused", "unauthorized", "denied"]):
                logs.append(line)
    except Exception:
        pass
    return logs

def analyze_log():
    if os.geteuid() != 0:
        warning("Please run the tool with sudo/root to access system logs!")
        return
    lines = load_logs()
    info(f"Loaded total log entries: {len(lines)}")
    section("Analysis: Failed Logins")
    failed_logins = analyze_failed_logins(lines)
    suspicious_found = False
    for ip, count in failed_logins.items():
        if count >= FAILED_THRESHOLD:
            warning(f"{ip} → {count} failed login attempts")
            suspicious_found = True
    if not suspicious_found:
        success("No suspicious failed login patterns detected")
    section("Analysis: Privilege Escalation")
    privilege_alerts = analyze_privilege_changes(lines)
    if privilege_alerts:
        for alert in privilege_alerts:
            warning(alert)
    else:
        success("No suspicious privilege escalation detected")
    section("Analysis: Sensitive File Changes")
    file_alerts = analyze_file_changes(lines)
    if file_alerts:
        for alert in file_alerts:
            warning(alert)
    else:
        success("No suspicious file changes detected")
    section("Analysis: Network Issues")
    network_alerts = analyze_network_issues(lines)
    if network_alerts:
        for alert in network_alerts:
            warning(alert)
    else:
        success("No suspicious network activity detected")
    section("Hints")
    if suspicious_found or privilege_alerts or file_alerts or network_alerts:
        hint("Multiple indicators detected, investigate further.")
    else:
        hint("No immediate threats detected, but continue monitoring.")

if __name__ == "__main__":
    analyze_log() 