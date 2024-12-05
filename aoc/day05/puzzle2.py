from aoc.day05 import is_rules_adhered_to, get_rules_and_prints


def solve():
    page_number_sum = 0
    rules, prints = get_rules_and_prints(False)
    for current_print in prints:
        pages = [int(page) for page in current_print.split(",")]
        if not is_rules_adhered_to(rules, pages):
            new_pages = _create_new_list_that_adheres_to_rules(rules, pages)
            middle_index = len(new_pages) // 2
            page_number_sum += new_pages[middle_index]
    print(page_number_sum)


def _create_new_list_that_adheres_to_rules(rules: dict[int, set[int]], pages: list[int]) -> list[int]:
    new_list = []
    for current_page in pages:
        has_to_be_before = rules.get(current_page, set())
        insert_index = len(new_list)
        for current_index in range(len(new_list), 0, -1):
            check_letter = new_list[current_index - 1]
            if check_letter in has_to_be_before:
                insert_index = new_list.index(check_letter)
        new_list.insert(insert_index, current_page)
    return new_list


if __name__ == "__main__":
    solve()
