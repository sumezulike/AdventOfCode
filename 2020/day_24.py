from enum import Enum
from pprint import pprint

from puzzles import day24 as puzzle


class Dir(Enum):
    EAST = 0
    S_EAST = 1
    S_WEST = 2
    WEST = 3
    N_WEST = 4
    N_EAST = 5


    def __repr__(self):
        return self.name

def paint(tiles: set[tuple[int, int]]):
    x, y = {t[0] for t in tiles}, {t[1] for t in tiles}
    frame = (min(x), max(x)), (min(y), max(y))
    x_d, y_d = -frame[0][0], -frame[1][0]
    n = [x for y in [neighbors(*t) for t in tiles] for x in y]
    for y in range(frame[1][1]+y_d):
        print("  "*(y%2), end="")
        for x in range(frame[0][1]+x_d):
            c = " "
            if (x-x_d, y-y_d) in tiles:
                c = "#"
            elif (x-x_d, y-y_d) in n:
                c = "."
            print(c, end="")
        print()

def parse_input(tiles: str) -> list[list[Dir]]:
    lines = []
    for line in tiles.split("\n"):
        t = []
        i = 0
        while i < len(line):
            if (c := line[i]) in "ew":
                t.append(Dir.EAST if c == "e" else Dir.WEST)
            else:
                t.append([[Dir.N_EAST, Dir.N_WEST], [Dir.S_EAST, Dir.S_WEST]][c == "s"][line[i + 1] == "w"])
                i += 1
            i += 1
        lines.append(t)
    return lines


def move(dirs: list[Dir]) -> tuple[int, int]:
    x = y = 0
    for d in dirs:
        if "N_" in d.name:
            y += 1
        elif "S_" in d.name:
            y -= 1

        if "EAST" in d.name:
            x += 1
        elif "WEST" in d.name:
            x -= 1

        if "EAST" == d.name:
            x += 1
        elif "WEST" == d.name:
            x -= 1

    return x, y


def neighbors(x, y) -> set[tuple[int, int]]:
    return {(x + 2, y), (x - 2, 0), (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)}


def step(black: set[tuple[int, int]]) -> set[tuple[int, int]]:
    white = set()
    for t in black:
        if (s := sum(n in black for n in neighbors(*t))) == 0 or s > 2:
            white.add(t)
    pot = set(x for y in (neighbors(*t) for t in black) for x in y if x not in black)
    flip = set(t for t in pot if sum(n in black for n in neighbors(*t)) == 2)
    black = (black - white) | flip
    return black


def test():
    ex = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

    tiles = set()
    lines = parse_input(ex)
    for l in lines:
        coords = move(l)
        if coords in tiles:
            tiles.remove(coords)
        else:
            tiles.add(coords)
    paint(tiles)
    print(len(tiles), "(10)")
    for i in range(100):
        tiles = step(tiles)
    paint(tiles)
    print(len(tiles), "(2208)")



def part_1() -> str:
    tiles = set()
    lines = parse_input(puzzle)
    for l in lines:
        coords = move(l)
        if coords in tiles:
            tiles.remove(coords)
        else:
            tiles.add(coords)
    return str(len(tiles))


def part_2() -> str:
    tiles = set()
    lines = parse_input(puzzle)
    for l in lines:
        coords = move(l)
        if coords in tiles:
            tiles.remove(coords)
        else:
            tiles.add(coords)
    tiles = step(tiles)
    print(len(tiles))


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
