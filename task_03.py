import sys
from collections import Counter

def parse_log_line(line: str) -> dict:
    """
    Парсить рядок логу та повертає словник з ключами:
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
    Зчитує лог-файл і повертає список словників для кожного рядка.
    """
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"❌ Файл '{file_path}' не знайдено.")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Повертає список логів певного рівня (наприклад, 'ERROR').
    """
    level = level.upper()
    return [log for log in logs if log["level"] == level]


def count_logs_by_level(logs: list) -> dict:
    """
    Підраховує кількість логів для кожного рівня логування.
    """
    levels = [log["level"] for log in logs]
    return dict(Counter(levels))


def display_log_counts(counts: dict):
    """
    Виводить результати у вигляді таблиці.
    """
    print("\n📊 Статистика логів за рівнями:\n")
    print(f"{'Рівень':<10} | {'Кількість':>10}")
    print("-" * 25)
    for level, count in counts.items():
        print(f"{level:<10} | {count:>10}")
    print("-" * 25)


def main():
    if len(sys.argv) < 2:
        print("🔹 Використання: python log_analyzer.py <шлях_до_файлу> [<рівень_логування>]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if len(sys.argv) == 3:
        # користувач вказав рівень логування
        level = sys.argv[2].upper()
        filtered = filter_logs_by_level(logs, level)
        if not filtered:
            print(f"⚠️  Записів рівня {level} не знайдено.")
        else:
            print(f"\n🔍 Логи рівня {level}:\n")
            for log in filtered:
                print(f"{log['date']} {log['time']} {log['level']} {log['message']}")
    else:
        # якщо рівень не вказано — виводимо статистику
        counts = count_logs_by_level(logs)
        display_log_counts(counts)


if __name__ == "__main__":
    main()
