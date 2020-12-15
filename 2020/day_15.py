from puzzles import day15 as puzzle
import timeit

indices = {}

def parse_input(numbers) -> list[int]:
    return [int(x) for x in numbers.split(",")]

def elves_game(numbers):
    global indices
    indices = {k: [i] for i, k in enumerate(numbers)}
    for i, x in enumerate(numbers):
        yield x
    while True:
        yield add_number(numbers)


def add_number(numbers: list[int]):
    pos = len(numbers) - 1
    n = numbers[pos]
    if indices[n] == [pos]:
        next = 0
    else:
        next = pos - indices[n][0]
    if next not in indices:
        indices[next] = []
    indices[next] = [*indices[next][-1:], pos + 1]
    numbers.append(next)
    return next


def test():
    test = [0, 3, 6]
    elves = elves_game(test)
    for i in range(1, 2020):
        next(elves)
    print(next(elves), "(436)")

def part_1() -> str:
    nums = parse_input(puzzle)
    elves = elves_game(nums)
    for i in range(1, 2020):
        next(elves)
    return str(next(elves))


def part_2() -> str:
    nums = parse_input(puzzle)
    elves = elves_game(nums)
    start = timeit.default_timer()
    for i in range(1, 30000000):
        next(elves)
    res = str(next(elves))
    end = timeit.default_timer()
    print(end-start)
    return res


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
