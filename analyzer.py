from collections import defaultdict
from formatter import info, warning, hint, section, success

FAILED_THRESHOLD = 3  # عدد محاولات الفشل قبل اعتبارها مشبوهة

def parse_line(line):
    """
    يحلل أي سطر لوج حقيقي.
    يدعم صيغ مثل:
    - تسجيل الدخول: 2026-04-03 08:15:23 LOGIN FAILED user=admin ip=192.168.1.50
    - sudo/root: user=john sudo: session opened
    - file change: /etc/passwd modified
    - network: connection refused from 192.168.1.100
    """
    data = {"raw": line, "type": None, "ip": "unknown", "user": "unknown", "status": None}

    if "LOGIN" in line:
        data["type"] = "login"
        data["status"] = "FAILED" if "FAILED" in line else "SUCCESS"
        for part in line.split():
            if part.startswith("user="):
                data["user"] = part.split("=")[1]
            elif part.startswith("ip="):
                data["ip"] = part.split("=")[1]

    elif "sudo" in line or "root" in line:
        data["type"] = "privilege"
        for part in line.split():
            if part.startswith("user="):
                data["user"] = part.split("=")[1]

    elif "modified" in line or "changed" in line:
        data["type"] = "file"

    elif "connection refused" in line or "unauthorized" in line or "denied" in line:
        data["type"] = "network"
        parts = line.split()
        for part in parts:
            if part.count('.') == 3:  # crude IP detection
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

def analyze_log(file_path):
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()

        info(f"Loaded file: {file_path}")
        info(f"Total log entries: {len(lines)}")

        # Failed logins
        section("Analysis: Failed Logins")
        failed_logins = analyze_failed_logins(lines)
        suspicious_found = False
        for ip, count in failed_logins.items():
            if count >= FAILED_THRESHOLD:
                warning(f"{ip} → {count} failed login attempts")
                suspicious_found = True
        if not suspicious_found:
            success("No suspicious failed login patterns detected")

        # Privilege changes
        section("Analysis: Privilege Escalation")
        privilege_alerts = analyze_privilege_changes(lines)
        if privilege_alerts:
            for alert in privilege_alerts:
                warning(alert)
        else:
            success("No suspicious privilege escalation detected")

        # File changes
        section("Analysis: Sensitive File Changes")
        file_alerts = analyze_file_changes(lines)
        if file_alerts:
            for alert in file_alerts:
                warning(alert)
        else:
            success("No suspicious file changes detected")

        # Network issues
        section("Analysis: Network Issues")
        network_alerts = analyze_network_issues(lines)
        if network_alerts:
            for alert in network_alerts:
                warning(alert)
        else:
            success("No suspicious network activity detected")

        # Hints
        section("Hints")
        if suspicious_found or privilege_alerts or file_alerts or network_alerts:
            hint("Multiple indicators detected, investigate further.")
        else:
            hint("No immediate threats detected, but continue monitoring.")

    except FileNotFoundError:
        warning("Log file not found!") 