from itertools import combinations

from puzzles import day9 as puzzle

puzzle = [int(i) for i in puzzle.split("\n")]


def test():
    test_puzzle = [int(i) for i in """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split("\n")]
    print(inv := find_invalid(test_puzzle, 5))
    print(s := find_bigger_sum(num=inv, numbers=test_puzzle))
    print(min(s)+max(s))


def find_sum(preamble: list[int], num: int) -> bool:
    valid = (sum(i) for i in combinations(preamble, 2))
    return num in valid


def find_invalid(numbers: list[int] = None, pre_len: int = 25) -> int:
    if numbers is None:
        numbers = puzzle
    preamble, numbers = numbers[:pre_len], numbers[pre_len:]
    for i in numbers:
        if not find_sum(preamble, i):
            return i
        preamble = preamble[1:] + [i]


def find_bigger_sum(numbers: list[int], num: int) -> list[int]:
    for i in range(len(numbers)):
        for length in range(len(numbers) - i):
            if t := sum(numbers[i:i + length]) == num:
                return numbers[i:i + length]
            elif t > num:
                break


def part_1() -> str:
    return str(find_invalid())


def part_2() -> str:
    inv = find_invalid()
    s = find_bigger_sum(numbers=puzzle, num=inv)
    return str(min(s) + max(s))


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
