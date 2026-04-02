import sys
from analyzer import analyze_log
from formatter import banner, info

def main():
    print("STARTED")

    banner()

    if len(sys.argv) != 2:
        info("Usage: python main.py <logfile>")
        return

    logfile = sys.argv[1]

    print("File received:", logfile)

    analyze_log(logfile)

if __name__ == "__main__":
    main()