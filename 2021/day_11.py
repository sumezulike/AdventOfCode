from puzzles import day11 as puzzle


def parse_puzzle(p: str) -> list[list[int]]:
    return [list(map(int, line)) for line in p.split("\n")]


def printg(grid: list[list[int]]):
    for row in grid:
        print("".join(str(x) for x in row))
    print()


def step(grid: list[list[int]]) -> tuple[list[list[int]], int]:
    flashes = 0


    def flash(x, y):
        nonlocal flashes
        flashes += 1
        for dx, dy in [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)]:
            _x, _y = x + dx, y + dy
            if 0 <= _x < len(grid[0]) and 0 <= _y < len(grid):
                grid[_y][_x] += 1
                if grid[_y][_x] == 10:
                    flash(_x, _y)


    for y, row in enumerate(grid):
        for x, oc in enumerate(row):
            grid[y][x] += 1
            if grid[y][x] == 10:
                flash(x, y)
    grid = [[0 if oc > 9 else oc for oc in row] for row in grid]
    return grid, flashes


def test():
    test_puzzle = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

    g = parse_puzzle(test_puzzle)
    flashes = []
    for i in range(100):
        g, f = step(g)
        print(f"After step {i + 1}:")
        printg(g)
        flashes.append(f)
    print(sum(flashes))


def part_1() -> str:
    g = parse_puzzle(puzzle)
    flashes = 0
    for i in range(100):
        g, f = step(g)
        flashes += f
    return str(flashes)


def part_2() -> str:
    i = 0
    g = parse_puzzle(puzzle)
    while True:
        i += 1
        g, f = step(g)
        if f == 100:
            return str(i)


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
