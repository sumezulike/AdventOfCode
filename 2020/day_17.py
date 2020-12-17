import itertools
from copy import deepcopy
from enum import Enum

from puzzles import day17 as puzzle


class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


class Space:
    def __init__(self, start: str = None):
        self.X_spaces: dict[XSpace] = dict()
        if start:
            self.set_start_layer(start)


    def __getitem__(self, item):
        if item not in self.X_spaces:
            self.X_spaces[item] = XSpace(space=self, pos=item)
        return self.X_spaces[item]


    def set_start_layer(self, start: str):
        for x, row in enumerate(start.split("\n")):
            for y, col in enumerate(row):
                self[x][y][0].state = State.ACTIVE if col == "#" else State.INACTIVE

    @property
    def active_cubes(self):
        active = 0
        for x in self.X_spaces.values():
            for y in x.Y_spaces.values():
                active += sum(y.cubes.values())
        return active


    @property
    def ready_cubes(self):
        active = 0
        for x in self.X_spaces.values():
            for y in x.Y_spaces.values():
                active += sum(c.next_state == State.ACTIVE for c in y.cubes.values())
        return active

    def step(self):
        prev = 0
        ready = None
        while ready != prev:
            for x in list(self.X_spaces.values()):
                for y in list(x.Y_spaces.values()):
                    for c in list(y.cubes.values()):
                        c.set_next_state()
            prev = ready
            ready = self.ready_cubes

        for x in self.X_spaces.values():
            for y in x.Y_spaces.values():
                for c in y.cubes.values():
                    c.step()

    def get_neighbours(self, pos: tuple[int, int, int]):
        return [self[pos[0] + x][pos[1] + y][pos[2] + z] for x, y, z in
                set(itertools.product((-1, 0, 1), repeat=3)) - {(0, 0, 0)}]


class XSpace:
    def __init__(self, space: Space, pos: int):
        self.Y_spaces: dict[YSpace] = dict()
        self.space = space
        self.pos = pos


    def __getitem__(self, item):
        if item not in self.Y_spaces:
            self.Y_spaces[item] = YSpace(space=self.space, x=self, pos=item)
        return self.Y_spaces[item]


class YSpace:
    def __init__(self, space: Space, x: XSpace, pos: int):
        self.cubes: dict[Cube] = dict()
        self.space = space
        self.x = x
        self.pos = pos


    def __getitem__(self, item):
        if item not in self.cubes:
            self.cubes[item] = Cube(state=State.INACTIVE, space=self.space, pos=(self.x.pos, self.pos, item))
        return self.cubes[item]


class Cube:

    def __init__(self, state: State, space: Space, pos: tuple[int, int, int]):
        self.space = space
        self.state = state
        self.pos = pos
        self.next_state = State.INACTIVE


    def __int__(self):
        return self.state.value


    def __add__(self, other):
        return int(self) + int(other)


    def __radd__(self, other):
        return int(self) + int(other)


    def __repr__(self):
        return "#" if self.active else "."


    @property
    def active(self):
        return self.state == State.ACTIVE


    def set_next_state(self):
        neighbors = self.space.get_neighbours(self.pos)
        if not self.active:
            if sum(neighbors) == 3:
                self.next_state = State.ACTIVE
            else:
                self.next_state = State.INACTIVE
        else:
            if 2 <= sum(neighbors) <= 3:
                self.next_state = State.ACTIVE
            else:
                self.next_state = State.INACTIVE


    def step(self):
        if type(self.next_state) != State:
            raise Exception(f"Next state is {self.next_state}")
        self.state = self.next_state
        self.next_state = None


def test():
    s = """.#.
..#
###"""
    space = Space(start=s)
    for i in range(2):
        print(i, space.active_cubes)
        space.step()
    print(space.active_cubes)



def part_1() -> str:
    space = Space(start=puzzle)
    for i in range(1, 7):
        space.step()
        print(i, space.active_cubes)
    return str(space.active_cubes)


def part_2() -> str:
    ...


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
