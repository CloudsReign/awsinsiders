# sip-stat-summary.py
# Counts SIP response codes from a basic SIP log

from collections import Counter
import sys

def parse_sip_responses(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    codes = []
    for line in lines:
        parts = line.strip().split()
        if parts and parts[0].isdigit() and len(parts[0]) == 3:
            codes.append(parts[0])

    summary = Counter(codes)
    for code, count in summary.items():
        print(f"{code}: {count} responses")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sip-stat-summary.py siplog.txt")
    else:
        parse_sip_responses(sys.argv[1])
