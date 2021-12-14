from collections import Counter

from puzzles import day14 as puzzle


def parse_puzzle2(p: str) -> tuple[Counter, dict[str, tuple[str, str]]]:
    return (lambda p1, p2: (Counter([p1[i - 1:i + 1] for i in range(1, len(p1))]), {a: (a[0] + b, b + a[1]) for a, b in [tuple(l.split(" -> ")) for l in p2.split("\n")]}))(*p.split("\n\n"))


def parse_puzzle(p: str) -> tuple[str, dict[str, str]]:
    return (lambda p1, p2: (p1, {a: b for a, b in [tuple(l.split(" -> ")) for l in p2.split("\n")]}))(*p.split("\n\n"))


def step2(state: Counter, instr: dict[str, tuple[str, str]]) -> Counter:
    new_state = Counter()
    for pair, n in state.items():
        new_state.update({p: n for p in instr[pair]})
    return new_state


def step(state: str, instr: dict[str, str]) -> str:
    new_state = ""
    for i, c in enumerate(state):
        if i < len(state) - 1:
            new_state += c + instr.get(c + state[i + 1], "")
        else:
            new_state += c
    return new_state


def test():
    test_puzzle = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
    o_state, _ = state, instr = parse_puzzle(test_puzzle)
    for _ in range(10):
        state = step(state, instr)

    state, instr = parse_puzzle2(test_puzzle)
    for _ in range(10):
        state = step2(state, instr)

    counts = Counter()
    for x, n in state.items():
        counts.update({x[0]: n})
        counts.update({x[1]: n})
    counts.update([o_state[0], o_state[-1]])

    most, *_, least = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    print(str(most[1] // 2 - least[1] // 2))


def part_1() -> str:
    state, instr = parse_puzzle(puzzle)
    for _ in range(10):
        state = step(state, instr)
    most, *_, least = sorted(Counter(state).items(), key=lambda x: x[1], reverse=True)
    return str(most[1] - least[1])


def part_2() -> str:
    o_state, _ = parse_puzzle(puzzle)
    state, instr = parse_puzzle2(puzzle)
    for i in range(40):
        state = step2(state, instr)
    counts = Counter()
    for x, n in state.items():
        counts.update({x[0]: n})
        counts.update({x[1]: n})
    counts.update([o_state[0], o_state[-1]])

    most, *_, least = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return str(most[1] // 2 - least[1] // 2)


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
