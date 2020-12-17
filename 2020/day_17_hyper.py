import itertools
import numpy as np
from puzzles import day17 as puzzle


SIZE = 20
SURROUNDING = set(itertools.product((-1, 0, 1), repeat=4)) - {(0, 0, 0, 0)}

class Space:
    def __init__(self, start: str = None):
        self.spaces = np.zeros((SIZE, SIZE, SIZE, SIZE), dtype=np.int8)
        if start:
            self.set_start_layer(start)


    def set_start_layer(self, start: str):
        for x, row in enumerate(start.split("\n")):
            for y, col in enumerate(row):
                self.spaces[x, y, 0, 0] = 1 if col == "#" else 0


    @property
    def active_cubes(self):
        active = (self.spaces == 1).sum()
        active_plus = (self.spaces == 3).sum()
        return active+active_plus


    @property
    def ready_cubes(self):
        ready = (self.spaces == 2).sum()
        ready_plus = (self.spaces == 3).sum()
        return ready+ready_plus


    def step(self):
        prev = 0
        ready = None
        while ready != prev:
            for x in range(SIZE):
                for y in range(SIZE):
                    for z in range(SIZE):
                        for w in range(SIZE):
                            self.set_next_state(x, y, z, w)
            prev = ready
            ready = self.ready_cubes

        for x in range(SIZE):
            for y in range(SIZE):
                for z in range(SIZE):
                    for w in range(SIZE):
                        self.step_cube(x, y, z, w)


    def get_neighbours(self, pos: tuple[int, int, int, int]):
        return [self.spaces[(pos[0] + x) % SIZE, (pos[1] + y) % SIZE, (pos[2] + z) % SIZE, (pos[3] + w) % SIZE]
                for x, y, z, w in SURROUNDING]


    def set_next_state(self, x, y, z, w):
        c = self.spaces[x, y, z, w]
        neighbors = self.get_neighbours((x, y, z, w))
        active = sum(n & 1 for n in neighbors)
        if not c & 1:
            if active == 3:
                self.spaces[x, y, z, w] = c | 2
            else:
                self.spaces[x, y, z, w] = c & 1
        else:
            if 2 <= active <= 3:
                self.spaces[x, y, z, w] = c | 2
            else:
                self.spaces[x, y, z, w] = c & 1


    def step_cube(self, x, y, z, w):
        self.spaces[x, y, z, w] >>= 1


class XSpace:
    def __init__(self, space: Space, pos: int):
        self.space = space
        self.pos = pos
        self.Y_spaces: list[YSpace] = [YSpace(space=self.space, x=self, pos=i) for i in range(SIZE)]


    def __getitem__(self, item):
        return self.Y_spaces[item + SIZE // 2]


class YSpace:
    def __init__(self, space: Space, x: XSpace, pos: int):
        self.space = space
        self.x = x
        self.pos = pos
        self.Z_spaces: list[ZSpace] = [ZSpace(space=self.space, x=self.x, y=self, pos=i) for i in range(SIZE)]


    def __getitem__(self, item):
        return self.Z_spaces[item + SIZE // 2]


class ZSpace:
    def __init__(self, space: Space, x: XSpace, y: YSpace, pos: int):
        self.space = space
        self.x = x
        self.y = y
        self.pos = pos
        self.cubes: list[int] = [0 for _ in range(SIZE)]


    def __getitem__(self, item):
        return self.cubes[item + SIZE // 2]

    def __setitem__(self, key, value):
        self.cubes[key + SIZE//2] = value

def test():
    s = """.#.
..#
###"""
    space = Space(start=s)
    for i in range(1, 7):
        space.step()
        print(i, space.active_cubes)
    print("(848)")



def part_1() -> str:
    ...


def part_2() -> str:
    space = Space(start=puzzle)
    for i in range(1, 7):
        space.step()
        print(i, space.active_cubes)
    return str(space.active_cubes)


if __name__ == '__main__':
 #   test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
