from typing import List


def read_rows(file_path: str) -> List[List[str]]:
    with open(file_path, 'r') as f:
        f_content = [line.strip().split() for line in f.readlines()]
    return f_content


def calc_safe_report(reports) -> int:
    safe = 0
    for report in reports:
        if is_monotonic(report) and check_diff(report):
            safe += 1
    return safe


def is_monotonic(arr: List[int]) -> bool:
    return all((int(i) < int(j) for i, j in zip(arr, arr[1:]))) or all((int(i) > int(j) for i, j in zip(arr, arr[1:])))


def check_diff(arr: List[int]) -> bool:
    return all(1 <= abs(int(i) - int(v)) <= 3 for i, v in zip(arr, arr[1:]))


print(calc_safe_report(read_rows('input.txt')))


# Part 2

def problem_damper(reports) -> int:
    safe = 0
    for report in reports:
        if is_monotonic(report) and check_diff(report):
            safe += 1
        else:
            for i in range(len(report)):
                modified_report = report[:i] + report[i+1:]
                if is_monotonic(modified_report) and check_diff(modified_report):
                    safe += 1
                    break
    return safe


print(problem_damper(read_rows('input.txt')))
