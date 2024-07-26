#!/usr/bin/python3
import sys
import signal

total_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0


def print_stats():
    """Print accumulated metrics."""
    global total_size, status_counts
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C) to print stats and exit."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 10:
                continue

            ip, dash, date, get, projects, http, status, file_size = (
                parts[0], parts[1], parts[2], parts[3],
                parts[4], parts[5], parts[8], parts[9]
            )

            status = int(status)
            file_size = int(file_size)

            if status in status_counts:
                status_counts[status] += 1

            total_size += file_size
            line_count += 1

            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            continue

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

