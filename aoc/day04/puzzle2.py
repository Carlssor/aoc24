from aoc import read_puzzle_input


MAS = "MAS"


def solve():
    total_occurrences = 0
    positions = dict((x, set()) for x in MAS)
    letters = read_puzzle_input()
    for row, line in enumerate(letters):
        for col, char in enumerate(line):
            if char in MAS:
                positions[char].add((col, row))
    for a_position in positions["A"]:
        num_mas_for_this_a = 0
        for m_col_offset in (-1, 1):
            for m_row_offset in (-1, 1):
                if _spells_mas(positions, a_position, (m_col_offset, m_row_offset)):
                    num_mas_for_this_a += 1
        total_occurrences += 1 if num_mas_for_this_a == 2 else 0
    print(total_occurrences)


def _spells_mas(
        positions: dict[str, set[tuple[int, int]]],
        a_position: tuple[int, int],
        m_offset: tuple[int, int]):
    m_position = (a_position[0] + m_offset[0], a_position[1] + m_offset[1])
    s_position = (a_position[0] + m_offset[0] * -1, a_position[1] + m_offset[1] * -1)
    return m_position in positions["M"] and s_position in positions["S"]



if __name__ == "__main__":
    solve()