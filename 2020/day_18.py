import regex
from puzzles import day18 as puzzle


def dumb_calc(expr: str) -> int:
    parenth = regex.findall(r"\(((?>[^()]+|(?R))*)\)", expr)
    for p in parenth:
        expr = expr.replace(f"({p})", str(dumb_calc(p)))
    while len(sp := expr.split()) > 1:
        expr = expr.replace(" ".join((sp[0], sp[1], sp[2])),
                            str(int(sp[0]) + int(sp[2])) if sp[1] == "+" else str(int(sp[0]) * int(sp[2])), 1)
    return int(expr)


def dumber_calc(expr: str) -> int:
    parenth = regex.findall(r"\(((?>[^()]+|(?R))*)\)", expr)
    for p in parenth:
        expr = expr.replace(f"({p})", str(dumber_calc(p)))
    plus = regex.findall(r"(\d+(?:\s\+\s\d+)+)", expr)
    for p in plus:
        expr = expr.replace(f"{p}", str(eval(p)))
    while len(sp := expr.split()) > 1:
        expr = expr.replace(" ".join((sp[0], sp[1], sp[2])),
                            str(int(sp[0]) + int(sp[2])) if sp[1] == "+" else str(int(sp[0]) * int(sp[2])), 1)
    return int(expr)




def test():
    tests1 = [
        ("2 * 3 + (4 * 5) ", 26),
        ("5 + (8 * 3 + 9 + 3 * 4 * 3) ", 437),
        ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) ", 12240),
        ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 ", 13632)
    ]

    tests2 = [
        ("1 + (2 * 3) + (4 * (5 + 6)) ", 51),
        ("2 * 3 + (4 * 5) ", 46),
        ("5 + (8 * 3 + 9 + 3 * 4 * 3) ", 1445),
        ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) ", 669060),
        ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 ", 23340),
    ]

    for t, s in tests1:
        r = dumb_calc(t)
        print(f"({['Correct', str(s)][s != r]:7}) {t} = {r}")
    print("---")
    for t, s in tests2:
        r = dumber_calc(t)
        print(f"({['Correct', str(s)][s != r]:7}) {t} = {r}")


def part_1() -> str:
    return str(sum(dumb_calc(line) for line in puzzle.split("\n")))


def part_2() -> str:
    return str(sum(dumber_calc(line) for line in puzzle.split("\n")))


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
