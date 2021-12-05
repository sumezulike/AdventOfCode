from contextlib import suppress

from puzzles import day4 as puzzle

def parse_puzzle(p: str) -> tuple[list[int], list[list[list[int]]]]:
    nums, *bingos = p.split("\n\n")
    nums = [int(x) for x in nums.split(",")]

    bingos = [[[int(c) for c in row.split()] for row in bingo.split("\n")] for bingo in bingos]
    return nums, bingos

def do_bingos(nums, bingos: list[list[list[int]]]) -> tuple[list[list[int]], int]:
    bingos.extend([[list(z) for z in zip(*b)] for b in bingos])

    for n in nums:
        for b in bingos:
            for row in b:
                with suppress(ValueError):
                    row.remove(n)
                if not row:
                    return b, n


def do_bingos_last(nums, bingos: list[list[list[int]]]) -> tuple[list[list[int]], int]:
    bingos_t = [[list(z) for z in zip(*b)] for b in bingos]

    for n in nums:
        for b in bingos.copy():
            bt = bingos_t[bingos.index(b)]
            for row in b:
                with suppress(ValueError):
                    row.remove(n)
                if not row:
                    if len(bingos) > 1:
                        bingos_t.remove(bt)
                        bingos.remove(b)
                        break
                    else:
                        return b, n
            else:
                for row in bt:
                    with suppress(ValueError):
                        row.remove(n)
                    if not row:
                        if len(bingos) > 1:
                            bingos.remove(b)
                            bingos_t.remove(bt)
                            break
                        else:
                            return b, n

def test():
    test_puzzle = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
    n, b = parse_puzzle(test_puzzle)
    rest, n = do_bingos(n, b)
    s = sum(sum(r) for r in rest)
    print(s, n, s * n)


    n, b = parse_puzzle(test_puzzle)
    rest, n = do_bingos_last(n, b)
    s = sum(sum(r) for r in rest)
    print(s, n, s * n)

def part_1() -> str:
    n, b = parse_puzzle(puzzle)
    rest, n = do_bingos(n, b)
    s = sum(sum(r) for r in rest)
    return str(s * n)

def part_2() -> str:
    n, b = parse_puzzle(puzzle)
    rest, n = do_bingos_last(n, b)
    s = sum(sum(r) for r in rest)
    return str(s * n)


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
