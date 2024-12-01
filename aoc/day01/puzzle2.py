from aoc import read_puzzle_input


def solve():
    similarity_score = 0
    left_frequency, right_frequency = {}, {}
    for list_pair in read_puzzle_input():
        left, right = [int(x) for x in list_pair.split()]
        left_frequency[left] = left_frequency.get(left, 0) + 1
        right_frequency[right] = right_frequency.get(right, 0) + 1
    for value, left_frequency in left_frequency.items():
        similarity_score += value * left_frequency * right_frequency.get(value, 0)
    print(similarity_score)


if __name__ == "__main__":
    solve()
