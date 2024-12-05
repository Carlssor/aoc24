import re

from aoc import read_puzzle_input


def solve():
    multiplication_sum = 0
    memory = "".join(read_puzzle_input())
    for x in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", memory):
        multiplication_sum += int(x.group(1)) * int(x.group(2))
    print(multiplication_sum)


if __name__ == "__main__":
    solve()