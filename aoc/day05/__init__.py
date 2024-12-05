from aoc import read_puzzle_input


def get_rules_and_prints(example: bool = False) -> tuple[dict[int, set[int]], list[str]]:
    found_delimiter = False
    rules, prints = {}, []
    for line in read_puzzle_input(example):
        if line.strip() == "":
            found_delimiter = True
            continue
        if not found_delimiter:
            page_must_be_before, other_page = [int(x) for x in line.split("|")]
            rules.setdefault(page_must_be_before, set()).add(other_page)
        else:
            prints.append(line.strip())
    return rules, prints


def is_rules_adhered_to(rules: dict[int, set[int]], pages: list[int]) -> bool:
    for current_page_index, current_page in enumerate(pages):
        restrictions = rules.get(current_page, set())
        for restriction in restrictions:
            if restriction not in pages:
                continue
            restricted_page_index = pages.index(restriction)
            if restricted_page_index < current_page_index:
                return False
    return True
