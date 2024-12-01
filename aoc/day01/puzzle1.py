from aoc import read_puzzle_input


def solve():
    total_distance = 0
    left_list, right_list = [], []
    for list_pair in read_puzzle_input():
        left_value, right_value = list_pair.split()
        left_list.append(int(left_value))
        right_list.append(int(right_value))
    for left_value, right_value in zip(sorted(left_list), sorted(right_list)):
        total_distance += abs(right_value - left_value)
    print(total_distance)


if __name__ == "__main__":
    solve()