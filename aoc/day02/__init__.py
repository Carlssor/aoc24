from functools import cache

@cache
def is_safe_record(*levels: tuple[int]):
    if levels[0] == levels[1]:
        return False
    should_increase = levels[0] < levels[1]
    diffs = map(lambda x: x[1] - x[0], zip(levels, levels[1:]))
    return all(1 <= diff <= 3 for diff in diffs) if should_increase else all(-3 <= diff <= -1 for diff in diffs)
