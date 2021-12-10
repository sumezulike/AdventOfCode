from statistics import median

from puzzles import day10 as puzzle

OPEN = "([{<"
CLOSE = ")]}>"
closing = {o: c for o, c in zip(OPEN, CLOSE)}

values1 = {c: v for c, v in zip(CLOSE, [3, 57, 1197, 25137])}
values2 = {c: v for c, v in zip(CLOSE, [1, 2, 3, 4])}


def completion_value(comp: str) -> int:
    val = 0
    for c in comp:
        val *= 5
        val += values2[c]
    return val


def parse_puzzle(p: str) -> list[str]:
    return p.split("\n")


def parse_lines(lines: list[str]) -> list[tuple[bool, str]]:
    def parse_line(line: str) -> tuple[bool, str]:
        stack = []
        for c in line:
            if c in OPEN:
                stack.append(c)
            else:
                if closing[stack[-1]] == c:
                    stack.pop()
                else:
                    return False, c
        else:
            return True, "".join(closing[c] for c in stack[::-1])


    return list(map(parse_line, lines))


def test():
    test_puzzle = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
    parsed = parse_lines(parse_puzzle(test_puzzle))
    errors = [l[1] for l in parsed if l[0] is False]
    completions = [l[1] for l in parsed if l[0] is True]
    print(errors)
    print(sum(values1[e] for e in errors))
    print(completions)
    print(median(map(completion_value, completions)))


def part_1() -> str:
    parsed = parse_lines(parse_puzzle(puzzle))
    errors = [l[1] for l in parsed if l[0] is False]
    return str(sum(values1[e] for e in errors))


def part_2() -> str:
    parsed = parse_lines(parse_puzzle(puzzle))
    completions = [l[1] for l in parsed if l[0] is True]
    return str(median(map(completion_value, completions)))


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
