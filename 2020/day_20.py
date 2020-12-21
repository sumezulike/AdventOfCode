import re

from puzzles import day20 as puzzle
from puzzles import day20test as test_input

class Tile:
    def __init__(self, number: int, layout: str):
        self.number = number

    def __repr__(self):
        return f"Tile ({self.number})"

def parse_input(tiles_str: str) -> list[Tile]:
    tiles = tiles_str.split("\n\n")
    tile_objects = []
    for t in tiles:
        title, tile = t.split("\n", 1)
        number = int(re.findall(r"\d+", title)[0])
        tile_objects.append(Tile(number=number, layout=tile))
    return tile_objects

def test():
    print(parse_input(test_input))

def part_1() -> str:
    pass

def part_2() -> str:
    pass


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
