from aoc import read_puzzle_input


XMAS = "XMAS"


def solve():
    total_occurrences = 0
    positions = dict((x, set()) for x in XMAS)
    letters = read_puzzle_input()
    for row, line in enumerate(letters):
        for col, char in enumerate(line):
            if char in XMAS:
                positions[char].add((col, row))
    for current_char_position in positions["X"]:
        for grow_col in (-1, 0, 1):
            for grow_row in (-1, 0, 1):
                if _spells_xmas(positions, current_char_position, (grow_col, grow_row)):
                    total_occurrences += 1
    print(total_occurrences)


def _spells_xmas(
        positions: dict[str, set[tuple[int, int]]],
        start: tuple[int, int],
        grow: tuple[int, int],
        current_letter: str=XMAS[0]):
    if current_letter == XMAS[-1]:
        return True
    col, row = start
    next_col, next_row = col + grow[0], row + grow[1]
    if (next_col, next_row) in positions[XMAS[XMAS.index(current_letter) + 1]]:
        return _spells_xmas(positions, (next_col, next_row), grow, XMAS[XMAS.index(current_letter) + 1])
    return False



if __name__ == "__main__":
    solve()