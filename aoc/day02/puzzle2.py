from aoc import read_puzzle_input
from aoc.day02 import is_safe_record


def solve():
    safe_reports = 0
    for report in read_puzzle_input(False):
        levels = [int(x) for x in report.split()]
        if is_safe_record(*levels):
            safe_reports += 1
        else:
            for remove_index in range(len(levels)):
                if is_safe_record(*levels[:remove_index] + levels[remove_index + 1:]):
                    safe_reports += 1
                    break

    print(f"Safe reports: {safe_reports}")


if __name__ == "__main__":
    solve()