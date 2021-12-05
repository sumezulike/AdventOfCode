from collections import defaultdict, Counter
from itertools import zip_longest
from pprint import pprint

from puzzles import day5 as puzzle


def parse_puzzle(p: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    return [((int(x1), int(x2)), (int(y1), int(y2))) for x1, y1, x2, y2 in
            [l.replace(" ", "").replace("->", ",").split(",") for l in p.split("\n")]]


def count_hits(coords: list[tuple[tuple[int, int], tuple[int, int]]], diag=False):
    valid = [(x, y) for x, y in coords if x[0] == x[1] or y[0] == y[1]] if not diag else coords
    hits = Counter()
    for x, y in valid:
        yr = -1 if y[0] > y[1] else 1
        xr = -1 if x[0] > x[1] else 1
        for _y, _x in zip_longest(range(y[0], y[1]+(yr*1), yr), range(x[0], x[1]+(xr*1), xr), fillvalue=[x[0], y[0]][y[0] == y[1]]):
            hits.update({(_x, _y): 1})
    return hits


def draw_hits(hits):
    xm, ym = zip(*hits.keys())
    xm, ym = max(xm)+1, max(ym)+1
    m = [["." for _ in range(ym)] for _ in range(xm)]
    for c, i in hits.items():
        m[c[1]][c[0]] = str(i)
    print("\n".join("".join(str(c) for c in h) for h in m))


def test():
    test_puzzle = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
    p = parse_puzzle(test_puzzle)
    h = count_hits(p)
    draw_hits(h)
    d = len([v for v in h.values() if v > 1])
    print(d)

def part_1() -> str:
    p = parse_puzzle(puzzle)
    h = count_hits(p)
    draw_hits(h)
    d = len([v for v in h.values() if v > 1])
    return str(d)

def part_2() -> str:
    p = parse_puzzle(puzzle)
    h = count_hits(p, True)
    draw_hits(h)
    d = len([v for v in h.values() if v > 1])
    return str(d)


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
