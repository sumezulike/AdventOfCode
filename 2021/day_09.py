from pprint import pprint

from puzzles import day9 as puzzle

def parse_puzzle(p: str) -> list[list[int]]:
    return [list(map(int, line)) for line in p.split("\n")]

def adjacent(mat: list[list[int]], x: int, y: int) -> list[tuple[int, tuple[int, int]]]:
    ad = []
    if x > 0:
        ad.append((mat[y][x-1], (x-1, y)))
    if x < len(mat[y])-1:
        ad.append((mat[y][x+1], (x+1, y)))
    if y > 0:
        ad.append((mat[y-1][x], (x, y-1)))
    if y < len(mat)-1:
        ad.append((mat[y+1][x], (x, y+1)))
    return ad

def find_minima(mat) -> list[tuple[int, tuple[int, int]]]:
    return [(mat[y][x], (x, y)) for y in range(len(mat)) for x in range(len(mat[y])) if all(mat[y][x] < i for i,p in adjacent(mat, x, y))]

def sum_risk(minima: list[tuple[int, tuple[int, int]]]) -> int:
    return sum(m[0]+1 for m in minima)

def find_pools(mat: list[list[int]], minima: list[tuple[int, tuple[int, int]]]) -> list[set[tuple[int, int]]]:
    pools = []
    for m in minima:
        pool = {m}
        while True:
            p_len = len(pool)
            for _, (x, y) in pool.copy():
                for adj in adjacent(mat, x, y):
                    if adj[0] < 9:
                        pool.add(adj)
            if len(pool) == p_len:
                break
        pools.append(pool)
    return pools

def test():
    test_puzzle = """2199943210
3987894921
9856789892
8767896789
9899965678"""
    mat = parse_puzzle(test_puzzle)
    print(m:=find_minima(mat))
    print(sum_risk(m))
    pools =find_pools(mat, m)
    print([len(p) for p in pools])

def part_1() -> str:
    mat = parse_puzzle(puzzle)
    m = find_minima(mat)
    return str(sum_risk(m))

def part_2() -> str:
    mat = parse_puzzle(puzzle)
    m = find_minima(mat)
    pools = find_pools(mat, m)
    sizes = sorted((len(p) for p in pools), reverse=True)
    return str(sizes[0]*sizes[1]*sizes[2])


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
