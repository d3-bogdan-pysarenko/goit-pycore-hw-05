import sys
from collections import Counter

def parse_log_line(line: str) -> dict:
    """
    Get dictionary with keys from log row:
    date, time, level, message
    """
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return None
    date, time, level, message = parts
    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message
    }


def load_logs(file_path: str) -> list:
    """
    Reqding file and getting file rows
    """
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"File for this path is not found ->  '{file_path}'")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Return logs of set level
    """
    level = level.upper()
    return [log for log in logs if log["level"] == level]


def count_logs_by_level(logs: list) -> dict:
    """
    count logs for level
    """
    levels = [log["level"] for log in logs]
    return dict(Counter(levels))


def display_log_counts(counts: dict):
    """
    Display results as table
    """
    print("\nLog statisticks by level:\n")
    print(f"{'Level':<10} | {'Count':>10}")
    print("-" * 25)
    for level, count in counts.items():
        print(f"{level:<10} | {count:>10}")
    print("-" * 25)


def main():
    if len(sys.argv) < 2:
        print(" Improper use of file. Please use like in the example below:\n"
        "Example: python task_03.py <pathto file> [<chosen level to display>]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if len(sys.argv) == 3:
        # When desired level is given
        level = sys.argv[2].upper()
        filtered = filter_logs_by_level(logs, level)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        if not filtered:
            print(f"There is no mentioned level of errors {level} in the file")
        else:
            print(f"\nLogs for the type {level}:\n")
            for log in filtered:
                print(f"{log['date']} {log['time']} {log['level']} {log['message']}")
        


if __name__ == "__main__":
    main()
