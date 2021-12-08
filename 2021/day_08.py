from puzzles import day8 as puzzle


def parse_puzzle(p: str) -> list[tuple[list[str], list[str]]]:
    def parse_line(l: str):
        digits, out = l.split("|")
        return ["".join(sorted(d)) for d in digits.split()], ["".join(sorted(o)) for o in out.split()]


    return [parse_line(line) for line in p.split("\n")]


def count_1478(l: list[str]) -> int:
    return sum(1 for x in l if len(x) in (2, 3, 4, 7))


def decode(digits: list[str], out: list[str]) -> int:
    code = {
        1: [d for d in digits if len(d) == 2][0],
        4: [d for d in digits if len(d) == 4][0],
        7: [d for d in digits if len(d) == 3][0],
        8: [d for d in digits if len(d) == 7][0],
    }
    code[6] = [d for d in digits if len(d) == 6 and len(set(code[1]).intersection(set(d))) == 1][0]
    code[9] = [d for d in digits if len(d) == 6 and len(set(code[4]).intersection(set(d))) == 4][0]
    code[0] = [d for d in digits if len(d) == 6 and d not in (code[6], code[9])][0]

    code[3] = [d for d in digits if len(d) == 5 and len(set(code[1]).intersection(set(d))) == 2][0]
    code[2] = [d for d in digits if len(d) == 5 and not d == code[3] and len(set(code[6]).union(set(d))) == 7][0]
    code[5] = [d for d in digits if len(d) == 5 and d not in (code[2], code[3])][0]

    key = {v: k for k, v in code.items()}
    return int("".join(str(key[c]) for c in out))


def test():
    test_puzzle = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    print(count_1478(parse_puzzle(test_puzzle)[0][1]))
    print(decode(*(parse_puzzle(test_puzzle)[0])))


def part_1() -> str:
    return str(sum(count_1478(o) for d, o in parse_puzzle(puzzle)))


def part_2() -> str:
    return str(sum(decode(*p) for p in parse_puzzle(puzzle)))


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
