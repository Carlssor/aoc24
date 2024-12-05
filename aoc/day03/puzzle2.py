import re

from aoc import read_puzzle_input


def solve():
    multiplication_sum = 0
    enabled = True
    memory = "".join(read_puzzle_input())
    for x in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|don't|do", memory):
        if x.group(0) == "do":
            enabled = True
        elif x.group(0) == "don't":
            enabled = False
        else:
            if enabled:
                multiplication_sum += int(x.group(1)) * int(x.group(2))
    print(multiplication_sum)


if __name__ == "__main__":
    solve()