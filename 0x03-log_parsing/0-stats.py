#!/usr/bin/python3
"""Log parsing script"""
import sys
import re
from signal import signal, SIGINT

# Allowed status codes
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_counts = {}
total_size = 0
line_count = 0

def print_stats():
    """Print accumulated stats"""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))

try:
    for line in sys.stdin:
        line_count += 1
        match = re.search(
            r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)', line)

        if match:
            code = match.group(2)
            size = match.group(3)
            try:
                total_size += int(size)
                if code in valid_codes:
                    status_counts[code] = status_counts.get(code, 0) + 1
            except:
                pass  # Skip any conversion issues

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

# Final print if not a multiple of 10
print_stats()

