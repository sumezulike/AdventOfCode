from puzzles import day3 as puzzle
from statistics import multimode


def parse_puzzle(p: str) -> list[tuple[int]]:
    return [tuple(int(b) for b in c) for c in p.split("\n")]

def count_bits(p: list[tuple[int]], default=max):
    return [default(multimode(x)) for x in zip(*p)]

def get_bitwise_most(p: list[tuple[int]]):
    i = 0
    while len(p) > 1:
        p = [x for x in p if x[i] == count_bits(p, max)[i]]
        i += 1
    return p[0]


def get_bitwise_least(p: list[tuple[int]]):
    i = 0
    while len(p) > 1:
        p = [x for x in p if x[i] != count_bits(p, max)[i]]
        i += 1
    return p[0]


def test():
    test_puzzle = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    test_puzzle = parse_puzzle(test_puzzle)
    print(count_bits(test_puzzle))
    print(get_bitwise_most(test_puzzle))
    print(get_bitwise_least(test_puzzle))


def part_1() -> str:
    most_common = count_bits(parse_puzzle(puzzle))
    gamma = int("".join(str(i) for i in most_common), 2)
    epsilon = (1 << len(most_common)) - 1 - gamma

    return str(gamma * epsilon)

def part_2() -> str:
    p = parse_puzzle(puzzle)

    oxy = int("".join(str(i) for i in get_bitwise_most(p)), 2)
    co2 = int("".join(str(i) for i in get_bitwise_least(p)), 2)
    return str(oxy*co2)

if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
