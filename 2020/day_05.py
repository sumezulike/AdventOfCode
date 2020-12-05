from puzzles import day5 as puzzle

def get_row_col(code: str) -> tuple[int, int]:
    row, col = code[:-3], code[-3:]
    row_num = int("".join(str(int(r == "B")) for r in row), 2)
    col_num = int("".join(str(int(c == "R")) for c in col), 2)
    return row_num, col_num

def get_seat_id(code: str) -> int:
    return sum((c in "BR")*2**i for i, c in enumerate(code[::-1]))

def part_1() -> str:
    return str(max(get_seat_id(c) for c in puzzle.split("\n")))

def part_2():
    existing = {get_seat_id(c) for c in puzzle.split("\n")}
    missing = set(range(min(existing), max(existing))) - existing
    return missing

def test():
    tests = {
        "BFFFBBFRRR": (70, 7, 567),
        "FFFBBBFRRR": (14, 7, 119),
        "BBFFBBFRLL": (102, 4, 820),
    }
    for t in tests.items():
        r, c = get_row_col(t[0])
        id = get_seat_id(t[0])
        assert (r, c, id) == t[1]

if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
