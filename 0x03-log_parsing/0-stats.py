#!/usr/bin/python3
"""Log parsing script"""

import sys
import signal


total_size = 0
status_codes = {}
line_count = 0

valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']


def print_stats():
    """Prints the accumulated statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """Handles keyboard interrupt (CTRL + C)"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split()

        if len(parts) < 7:
            continue

        try:
            status = parts[-2]
            size = int(parts[-1])
            total_size += size

            if status in valid_codes:
                status_codes[status] = status_codes.get(status, 0) + 1
        except Exception:
            continue

        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
