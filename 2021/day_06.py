from puzzles import day6 as puzzle


def parse_puzzle(p: str) -> list[int]:
    return [int(x) for x in p.split(",")]


def simulate_growth(state: list[int], days=80):
    def step(s):
        return [x - 1 if x else 6 for x in s] + [8] * s.count(0)


    for _ in range(days):
        state = step(state)
    return state


def simulate_growth2(state: list[int], days=80):
    state = [state.count(i) for i in range(9)]

    def step(s):
        s1 = [s[i+1] for i in range(8)] + [s[0]]
        s1[6] += s[0]
        return s1

    for i in range(days):
        state = step(state)
    return state


def test():
    test_puzzle = "3,4,3,1,2"
    test_puzzle = parse_puzzle(test_puzzle)
    print(len(simulate_growth(test_puzzle, 80)))


def part_1() -> str:
    return str(len(simulate_growth(parse_puzzle(puzzle), 80)))


def part_2() -> str:
    return str(sum(simulate_growth2(parse_puzzle(puzzle), 256)))


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
