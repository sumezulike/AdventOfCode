from puzzles import day17 as puzzle
import matplotlib.pyplot as plt

sol2 = [(int(p.split(",")[0]), int(p.split(",")[1])) for p in """23,-10  25,-9   27,-5   29,-6   22,-6   21,-7   9,0     27,-7   24,-5
25,-7   26,-6   25,-5   6,8     11,-2   20,-5   29,-10  6,3     28,-7
8,0     30,-6   29,-8   20,-10  6,7     6,4     6,1     14,-4   21,-6
26,-10  7,-1    7,7     8,-1    21,-9   6,2     20,-7   30,-10  14,-3
20,-8   13,-2   7,3     28,-8   29,-9   15,-3   22,-5   26,-8   25,-8
25,-6   15,-4   9,-2    15,-2   12,-2   28,-9   12,-3   24,-6   23,-7
25,-10  7,8     11,-3   26,-7   7,1     23,-9   6,0     22,-10  27,-6
8,1     22,-8   13,-4   7,6     28,-6   11,-4   12,-4   26,-9   7,4
24,-10  23,-8   30,-8   7,0     9,-1    10,-1   26,-5   22,-9   6,5
7,5     23,-6   28,-10  10,-2   11,-1   20,-9   14,-2   29,-7   13,-3
23,-5   24,-8   27,-9   30,-7   28,-5   21,-10  7,9     6,6     21,-5
27,-10  7,2     30,-9   21,-8   22,-7   24,-9   20,-6   6,9     29,-5
8,-2    27,-8   30,-5   24,-7""".replace("\n", " ").split()]

def parse_puzzle(p: str) -> tuple[tuple[int, int], tuple[int, int]]:
    return tuple(map(lambda x: tuple(map(int, x.split("=")[1].split(".."))), p.replace(",", "").split()[2:]))

def f(x, y, dx, dy) -> tuple[int, int, int, int]:
    x += dx
    y += dy
    dx = dx - 1 if dx > 0 else dx + 1 if dx < 0 else dx
    dy -= 1
    return x, y, dx, dy

def shoot(dx: int, dy: int, target) -> tuple[bool, int]:
    x, y = 0, 0
    i = 0
    while True:
        i += 1
        x, y, dx, dy = f(x, y, dx, dy)
        if target[0][0] <= x <= target[0][1] and target[1][0] <= y <= target[1][1]:
            return True, i
        if x > target[0][1] or y < target[1][0]:
            return False, i

def test():
    test_puzzle = "target area: x=20..30, y=-10..-5"
    target_area = parse_puzzle(test_puzzle)

    hits = []
    fig, ax = plt.subplots()
    for x in range(target_area[0][1]+1):
        for y in range(target_area[1][0], target_area[0][1]):
            hit, i = shoot(x, y, target_area)
            d = 0, 0, x, y
            traj = [(d := f(*d)) for _ in range(i)]
            pos = list(zip(*([(0, 0)] + [(t[0], t[1]) for t in traj])))
            if hit:
                ax.plot(*pos, color="green", linestyle=":", marker="")
                hits.append((x, y))
    plt.show()
    print(len(hits))
    missing = [h for h in sol2 if h not in hits]
    print([(m, shoot(*m, target_area)) for m in missing])


def part_1() -> str:
    peaks = []
    target_area = parse_puzzle(puzzle)
    fig, ax = plt.subplots()
    for x in range(target_area[0][1]):
        for y in range(target_area[0][1]):
            hit, i = shoot(x, y, target_area)
            d = 0, 0, x, y
            traj = [(d := f(*d)) for _ in range(i)]
            pos = list(zip(*([(0, 0)] + [(t[0], t[1]) for t in traj])))
            if hit:
                ax.plot(*pos, color="green", linestyle=":", marker="")
                peaks.append(max(pos[1]))
    plt.show()
    return max(peaks)

def part_2() -> str:
    hits = []
    target_area = parse_puzzle(puzzle)
    fig, ax = plt.subplots()
    for x in range(target_area[0][1] + 1):
        for y in range(target_area[1][0], target_area[0][1]):
            hit, i = shoot(x, y, target_area)
            d = 0, 0, x, y
            traj = [(d := f(*d)) for _ in range(i)]
            pos = list(zip(*([(0, 0)] + [(t[0], t[1]) for t in traj])))
            if hit:
                ax.plot(*pos, color="green", linestyle=":", marker="")
                hits.append((x, y))
    plt.show()
    return len(hits)


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
