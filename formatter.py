def banner():
    print("\n" + "=" * 50)
    print("           LOGIXCTF ANALYZER")
    print("=" * 50)

def section(title):
    print(f"\n--- {title} ---")

def info(msg):
    print(f"[+] {msg}")

def warning(msg):
    print(f"[!] {msg}")

def success(msg):
    print(f"[✔] {msg}")

def hint(msg):
    print(f"[*] {msg}")