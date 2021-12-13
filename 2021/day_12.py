from collections import defaultdict
from functools import partial

from puzzles import day12 as puzzle


def parse_puzzle(p: str) -> dict[str, list[str]]:
    edges = [tuple(line.split("-")) for line in p.split("\n")]
    edges += [(b, a) for a, b in edges]
    edges = list(set(edges))
    neighbors = defaultdict(list)
    for e, n in edges:
        neighbors[e].append(n)
    return neighbors


def find_paths(neighbors: dict[str, list[str]], allow_repeat=False):
    res = []
    paths = [(["start"], allow_repeat)]
    while paths:
        new_paths = []
        for p in paths:
            for n in neighbors[p[0][-1]]:
                n_p = p[0]+[n]
                if n != "end":
                    if n.isupper() or n not in p[0]:
                        new_paths.append((n_p, p[1] and True))
                    else:
                        if p[1] and n != "start":
                            new_paths.append((n_p, False))
                else:
                    res.append(n_p)
        paths = new_paths
    return res


def test():
    test_puzzles = ("""start-A
start-b
A-c
A-b
b-d
A-end
b-end""",
    """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""",
    """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""")

    print(*tuple(map(len, map(find_paths, map(parse_puzzle, test_puzzles)))))
    print(*tuple(map(len, map(partial(find_paths, allow_repeat=True), map(parse_puzzle, test_puzzles)))))


def part_1() -> str:
    neighbors = parse_puzzle(puzzle)
    paths = find_paths(neighbors)
    return str(len(paths))


def part_2() -> str:
    neighbors = parse_puzzle(puzzle)
    paths = find_paths(neighbors, True)
    return str(len(paths))


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
