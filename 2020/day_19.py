import re

from puzzles import day19 as puzzle


def parse_rules(rules: str) -> dict[int, str]:
    return {int(l.split(":")[0]): l.split(": ", 1)[1] for l in rules.split("\n")}

def get_regex(rules: dict[int, str], rule_num: int = 0) -> str:
    regex = ""
    rule = rules[rule_num]
    if "|" in rule:
        l, r = rule.split("|", 1)
        l, r = [int(i) for i in l.split()], [int(i) for i in r.split()]
        regex += "("
        for i in l:
            regex += get_regex(rules, i)
        regex += "|"
        for i in r:
            regex += get_regex(rules, i)
        regex += ")"
    elif '"' in rule:
        regex += rule.replace('"', "")
    else:
        nums = [int(i) for i in rule.split()]
        for i in nums:
            regex += get_regex(rules, i)
    return regex

def test():
    tests = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""
    r, t = tests.split("\n\n", 1)
    r = parse_rules(r)
    reg = get_regex(r, 0)
    print(reg)
    for line in t.split("\n"):
        print(re.fullmatch(reg, line))


def part_1() -> str:
    r, t = puzzle.split("\n\n", 1)
    r = parse_rules(r)
    reg = get_regex(r, 0)
    print(reg)
    return str(sum(bool(re.fullmatch(reg, line)) for line in t.split("\n")))


def part_2() -> str:
    r, t = puzzle.split("\n\n", 1)
    r = r.replace("8: 42", "8: 42 | 42 8").replace("11: 42 31", "11: 42 31 | 42 11 31")
    r = parse_rules(r)
    reg = get_regex(r, 0)
    print(reg)
    return str(sum(bool(re.fullmatch(reg, line)) for line in t.split("\n")))


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
