from utils import read_file


def main():
    safe_reports = 0

    for report in read_file():
        if report_is_safe(report):
            safe_reports += 1

    return safe_reports


def report_is_safe(report):
    if len(report) < 2:
        return True
    should_increase = report[0] < report[1]

    for i in range(len(report) - 1):
        diff = report[i] - report[i + 1]
        if should_increase:
            diff *= -1

        if diff > 3 or diff < 1:
            return False

    return True


if __name__ == "__main__":
    print(f"number of safe reports: {main()}")  # 379
