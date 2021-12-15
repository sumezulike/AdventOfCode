import operator
from functools import reduce
import numpy as np

import retworkx
from retworkx import PyDiGraph

from puzzles import day15 as puzzle


def parse_puzzle(p: str) -> PyDiGraph:
    g = PyDiGraph()
    vals = [[int(c) for c in row] for row in p.split("\n")]
    pos_idx = {}
    for y, row in enumerate(vals):
        for x, v in enumerate(row):
            pos_idx[(x, y)] = g.add_node(v)
    for y, row in enumerate(vals):
        for x, v in enumerate(row):
            n = pos_idx[(x, y)]
            if x > 0:
                g.add_edge(n, pos_idx[(x - 1, y)], vals[y][x - 1])
            if y > 0:
                g.add_edge(n, pos_idx[(x, y - 1)], vals[y - 1][x])
            if x < len(row) - 1:
                g.add_edge(n, pos_idx[(x + 1, y)], vals[y][x + 1])
            if y < len(vals) - 1:
                g.add_edge(n, pos_idx[(x, y + 1)], vals[y + 1][x])
    return g


def extend_and_parse_puzzle(p: str) -> PyDiGraph:
    vals = [[int(c) for c in row] for row in p.split("\n")]

    vals = [reduce(operator.add, [[(x + i) if x+i <= 9 else (x+i-9) for x in row] for i in range(5)]) for row in vals]
    extended = []
    for i in range(0, 5):
        r = np.array(vals)+i
        r[r > 9] -= 9
        extended.extend(r)

    new_puzzle = "\n".join("".join(str(c) for c in row) for row in extended)
    return parse_puzzle(new_puzzle)


def test():
    test_puzzle = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
    g = parse_puzzle(test_puzzle)
    path = retworkx.dijkstra_shortest_paths(g, 0, len(g) - 1, weight_fn=float)
    print(sum(g[i] for i in list(path[len(g) - 1])[1:]))

    g = extend_and_parse_puzzle(test_puzzle)
    path = retworkx.dijkstra_shortest_paths(g, 0, len(g) - 1, weight_fn=float)
    print(sum(g[i] for i in list(path[len(g) - 1])[1:]))


def part_1() -> str:
    g = parse_puzzle(puzzle)
    path = retworkx.dijkstra_shortest_paths(g, 0, len(g) - 1, weight_fn=float)
    return str(sum(g[i] for i in list(path[len(g) - 1])[1:]))


def part_2() -> str:
    g = extend_and_parse_puzzle(puzzle)
    path = retworkx.dijkstra_shortest_paths(g, 0, len(g) - 1, weight_fn=float)
    return str(sum(g[i] for i in list(path[len(g) - 1])[1:]))


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
