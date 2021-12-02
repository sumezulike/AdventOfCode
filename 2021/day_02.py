from collections import Counter

from puzzles import day2 as puzzle


def test():
    test_puzzle = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
    print(execute(test_puzzle.split("\n")))
    print(execute_aim(test_puzzle.split("\n")))


def execute(commands: list[str]):
    c = Counter()
    for cmd in commands:
        d, v = cmd.split()
        c.update({d: int(v)})
    return c["forward"], c["down"]-c["up"]


def execute_aim(commands: list[str]):
    f = d = aim = 0
    for cmd in commands:
        c, v = cmd.split()
        v = int(v)
        aim += {"up": -1, "down": 1}.get(c, 0) * v
        if c == "forward":
            f += v
            d += v*aim
    return f, d


def part_1() -> str:
    f, d = execute(puzzle.split("\n"))
    return str(f*d)


def part_2() -> str:
    f, d = execute_aim(puzzle.split("\n"))
    return str(f*d)


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
