from typing import List


def read_file(file_path: str) -> List[List[int]]:
    try:
        with open(file_path, 'r') as file:
            return [list(map(int, line.strip().split())) for line in file if line.strip()]
    except ValueError:
        print(f"Error: Invalid data format in file {file_path}")
        return []


def is_report_safe(report: List[int]) -> bool:
    global_monotonicity = None  # -1 for decreasing, 1 for increasing
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        local_monotonicity = 1 if report[i] < report[i + 1] else -1
        if diff == 0 or diff > 3:
            return False
        if global_monotonicity is None:
            global_monotonicity = local_monotonicity
        elif global_monotonicity != local_monotonicity:
            return False
    return True


def calc_safe_reports(reports: List[List[int]], use_dampener: bool = False) -> int:
    total_safe_reports = 0
    for report in reports:
        if is_report_safe(report):
            total_safe_reports += 1
            continue
        if use_dampener:
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1:]
                if is_report_safe(modified_report):
                    total_safe_reports += 1
                    break
    return total_safe_reports


def process_reports(file_path: str, use_dampener: bool = False) -> None:
    reports = read_file(file_path)
    if not reports:
        print(f"No valid data in file: {file_path}")
        return
    safe_reports = calc_safe_reports(reports, use_dampener)
    print(f"Total safe reports: {safe_reports}")


def main() -> None:
    example_file_path = "../data/day2-example.txt"
    test_file_path = "../data/day2-test.txt"
    print("[Part 1]")
    print("Example:")
    process_reports(example_file_path)
    print("Test:")
    process_reports(test_file_path)
    print("\n[Part 2]")
    print("Example:")
    process_reports(example_file_path, use_dampener=True)
    print("Test:")
    process_reports(test_file_path, use_dampener=True)


if __name__ == "__main__":
    main()
