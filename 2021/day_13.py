from puzzles import day13 as puzzle


def parse_puzzle(p: str) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    return (lambda p1, p2: ([tuple(map(int, l1.split(","))) for l1 in p1.split("\n")], [(0, int(l2.split("=")[1]))[::(lambda b: b - (b < 1))("y" in l2)] for l2 in p2.split("\n")]))(*p.split("\n\n"))


def fold_points(points, folds):
    def fold_point(point, fold):
        dim = int(fold[1] > 0)
        if point[dim] > fold[dim]:
            point = list(point)
            point[dim] = fold[dim] - abs(point[dim] - fold[dim])
            point = tuple(point)
        return point


    for f in folds:
        points = list({fold_point(p, f) for p in points})
    return points


def print_points(points):
    for y in range(max(list(zip(*points))[1]) + 1):
        for x in range(max(list(zip(*points))[0]) + 1):
            print("#" if (x, y) in points else ".", end="")
        print()


def test():
    test_puzzle = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold_points along y=7
fold_points along x=5"""
    points, folds = parse_puzzle(test_puzzle)
    points = fold_points(points, folds)
    print_points(points)


def part_1() -> str:
    points, folds = parse_puzzle(puzzle)
    points = fold_points(points, folds[:1])
    return str(len(points))


def part_2() -> str:
    points, folds = parse_puzzle(puzzle)
    points = fold_points(points, folds)
    print_points(points)
    return "Tilt to read"


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
