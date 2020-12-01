import random
from time import sleep
from typing import List

WIDTH = 5
HEIGHT = 5


class Bugfield:
    def __init__(self, population: List[bool] = None, pattern: str = None):
        self.bugs = population
        if pattern:
            self.bugs = [x == "#" for x in pattern.replace("\n", "")]


    def get_field(self, x, y):
        if x < 0 or x > WIDTH - 1:
            return False
        if y < 0 or y > WIDTH - 1:
            return False
        return self.bugs[x + 5 * y]


    def set_field(self, x, y, value):
        if x < 0 or x > WIDTH - 1:
            return False
        if y < 0 or y > WIDTH - 1:
            return False
        self.bugs[x + WIDTH * y] = value
        return True


    def count_surrounding(self, x, y):
        return [self.get_field(x + i, y + j) for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]].count(True)


    def __str__(self):
        return "\n".join(["".join(["#" if self.get_field(x, y) else "." for x in range(WIDTH)]) for y in range(HEIGHT)])


    def step(self):
        temp = Bugfield(population=self.bugs)
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if temp.get_field(x, y):
                    if self.count_surrounding(x, y) != 1:
                        temp.set_field(x, y, False)
                else:
                    if 1 <= self.count_surrounding(x, y) <= 2:
                        temp.set_field(x, y, True)
        self.bugs = temp.bugs


EXAMPLE = """....#
#..#.
#..##
..#..
#...."""
PATTERN = """#..##
##...
.#.#.
#####
####.
"""


def part_1():
    b = Bugfield(pattern=EXAMPLE)
    for _ in range(4):
        print(b)
        print()
        b.step()

if __name__ == '__main__':
    part_1()
