import re

from puzzles import day7 as puzzle


def test():
    test_1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
    test_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""
    r1 = parse_bag_rules(test_1)
    r2 = parse_bag_rules(test_2)
    # pprint(r)
    res1 = count_bag_spaces(r1)
    print("Test 1: ", res1, "(4)")
    res2_1 = count_total_bags(r1)
    res2_2 = count_total_bags(r2)
    print("Test 2(1): ", res2_1, "(32)")
    print("Test 2(2): ", res2_2, "(126)")


def parse_bag_rules(puzzle=puzzle) -> dict[str: dict[str: int]]:
    bags = dict()
    for line in puzzle.split("\n"):
        container, *contained = re.findall(r"((?:\d+ )?\w+ \w+) bags?", line)
        bags[container] = {bag: int(num) if num.isdigit() else 0 for num, bag in
                           [c.split(" ", 1) for c in contained]}
    return bags


def count_bag_spaces(rules: dict, search: set[str] = None) -> int:
    if search is None:
        search = {"shiny gold"}
    searching = True
    while searching:
        searching = False
        for container, content in rules.items():
            if set(search) & set(list(content.keys())):
                if container not in search:
                    search.add(container)
                    searching = True
    return len(search) - 1


def count_total_bags(rules: dict, search: str = "shiny gold") -> int:
    content = rules.get(search)
    if sum(content.values()) == 0:
        return 1
    else:
        return 1+sum(n * count_total_bags(rules, b) for b, n in content.items())


def part_1() -> str:
    return str(count_bag_spaces(parse_bag_rules()))


def part_2() -> str:
    return str(count_total_bags(parse_bag_rules()))


if __name__ == '__main__':
    test()
    print()
    print("Part 1:")
    print(part_1())
    print()
    print("Part 2:")
    print(part_2())
