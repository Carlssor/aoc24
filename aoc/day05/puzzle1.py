from aoc.day05 import is_rules_adhered_to, get_rules_and_prints


def solve():
    page_number_sum = 0
    rules, prints = get_rules_and_prints()
    for current_print in prints:
        pages = [int(page) for page in current_print.split(",")]
        if is_rules_adhered_to(rules, pages):
            middle_index = len(pages) // 2
            page_number_sum += pages[middle_index]
    print(page_number_sum)


if __name__ == "__main__":
    solve()
