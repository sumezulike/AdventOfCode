from puzzles import day6 as puzzle

def test():
    p = """abc

a
b
c

ab
ac

a
a
a
a

b"""
    assert part_1(p) == "11"
    assert part_2(p) == "6"

def part_1(puzzle=puzzle) -> str:
    return str(sum(len(set(line)) for line in [batch.replace("\n", "").replace(" ", "") for batch in puzzle.split("\n\n")]))

def part_2(puzzle=puzzle) -> str:
    return str(sum(len(l) for l in list(set.intersection(*map(set, line)) for line in [batch.split("\n") for batch in puzzle.split("\n\n")])))


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
