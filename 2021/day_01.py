from puzzles import day1 as puzzle


def parse_input(p: str) -> list[int]:
    return [int(x) for x in p.split("\n")]


def count_increases(depths: list[int]) -> int:
    return sum(depths[i] > depths[i - 1] for i in range(1, len(depths)))


def to_sliding_window(values: list[int]) -> list[int]:
    return [sum(values[i:i+3]) for i in range(len(values)-2)]


def test():
    test_puzzle = """199
200
208
210
200
207
240
269
260
263"""
    print(count_increases(parse_input(test_puzzle)))
    print(count_increases(to_sliding_window(parse_input(test_puzzle))))

def part_1() -> str:
    return str(count_increases(parse_input(puzzle)))


def part_2() -> str:
    return str(count_increases(to_sliding_window(parse_input(puzzle))))


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
