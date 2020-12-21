import re
from pprint import pprint

from puzzles import day21 as puzzle


def parse_inputs(ingr: str) -> list[tuple[list[str], list[str]]]:
    allergens = r"\(contains (.+)\)"
    res = []
    for line in ingr.split("\n"):
        res.append((line.split("(", 1)[0].split(), re.findall(allergens, line)[0].split(", ")))
    return res


def translate_allergens(ingr: list[tuple[list[str], list[str]]]) -> dict[str, str]:
    d = dict()
    for stuff, allergens in ingr:
        for a in allergens:
            if a not in d:
                d[a] = set()
            for s in stuff:
                d[a].add(s)
    for stuff, allergens in ingr:
        for a in allergens:
            d[a] = d[a].intersection(set(stuff))

    again = True
    while again:
        again = False
        for allergen, names in d.items():
            if len(names) == 1 and any(names & v for v in d.values() if v != names):
                again = True
                d = {k: v - names if v != names else names for k, v in d.items()}
    return {k: list(v)[0] for k, v in d.items()}


def test():
    tests = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""
    l = parse_inputs(tests)
    d = translate_allergens(l)
    print(d)


def part_1() -> str:
    ingr = parse_inputs(puzzle)
    tr = translate_allergens(ingr)
    poison = set(tr.values())
    food = [y for x in ingr for y in x[0]]
    safe = set(food) - poison
    safe_food = [f for f in food if f in safe]
    return str(len(safe_food))

def part_2() -> str:
    ingr = parse_inputs(puzzle)
    tr = translate_allergens(ingr)
    tr = {v: k for k, v in tr.items()}
    poisons = sorted([n for n in tr], key=lambda n: tr[n])
    return ",".join(poisons)

if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
