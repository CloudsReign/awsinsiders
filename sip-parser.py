# sip-parser.py
# Simple SIP log parser to extract call IDs and message flow

import re

def parse_sip_trace(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    call_id = ""
    for line in lines:
        if "Call-ID:" in line:
            call_id = line.strip().split("Call-ID:")[-1].strip()
            print(f"\n--- Call-ID: {call_id} ---")
        elif line.startswith(("INVITE", "BYE", "ACK", "180", "200")):
            print(line.strip())

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python sip-parser.py <sip_log.txt>")
    else:
        parse_sip_trace(sys.argv[1])
