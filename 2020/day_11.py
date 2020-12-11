from enum import Enum
from typing import Optional

from puzzles import day11 as puzzle


class Space(Enum):
    Floor = 0
    Empty = 1
    Occupied = 2

rules = """
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
"""


class Seats:

    def __init__(self, seats: str):
        self.seats = self.parse_seats(seats)


    def parse_seats(self, seatstr: str) -> list[list[Space]]:
        seats = [
            [{".": Space.Floor, "L": Space.Empty, "#": Space.Empty}.get(c) for c in row]
            for row in seatstr.split("\n")
        ]
        return seats

    def get_seat(self, *, x, y) -> Optional[Space]:
        if y < 0 or y >= len(self.seats):
            return None
        if x < 0 or x >= len(self.seats[y]):
            return None
        return self.seats[y][x]

    def look_for_seat(self, *, x, y, direction: tuple) -> Optional[Space]:
        s = self.get_seat(x=x, y=y)
        i = 1
        while s is not None:
            s = self.get_seat(x=x + i*direction[0], y=y + i*direction[1])
            if s == Space.Occupied or s == Space.Empty:
                return s
            i += 1
        return s

    def get_adjacent(self, *, x, y) -> list[Optional[Space]]:
        return [self.get_seat(x=x+dx, y=y+dy) for dx, dy in [(-1,  1), (0,  1), (1,  1),
                                                             (-1,  0),          (1,  0),
                                                             (-1, -1), (0, -1), (1, -1)]]

    def get_visible(self, x, y):
        return [self.look_for_seat(x=x, y=y, direction=d) for d in [(-1,  1), (0,  1), (1,  1),
                                                                    (-1,  0),          (1,  0),
                                                                    (-1, -1), (0, -1), (1, -1)]]

    def step(self, version) -> bool:
        temp = [row.copy() for row in self.seats]
        for y, row in enumerate(self.seats):
            for x, col in enumerate(row):
                if version == 1:
                    temp[y][x] = self.check_seat(x=x, y=y)
                elif version == 2:
                    temp[y][x] = self.check_seat_2(x=x, y=y)
        changed = self.seats != temp
        self.seats = temp
        return changed

    def check_seat(self, *, x, y) -> Space:
        seat = self.get_seat(x=x, y=y)
        if seat == Space.Empty and not any(s == Space.Occupied for s in self.get_adjacent(x=x, y=y)):
            return Space.Occupied
        if seat == Space.Occupied and sum(s == Space.Occupied for s in self.get_adjacent(x=x, y=y)) >= 4:
            return Space.Empty
        return seat

    def check_seat_2(self, *, x, y) -> Space:
        seat = self.get_seat(x=x, y=y)
        if seat == Space.Empty and not any(s == Space.Occupied for s in self.get_visible(x=x, y=y)):
            return Space.Occupied
        if seat == Space.Occupied and sum(s == Space.Occupied for s in self.get_visible(x=x, y=y)) >= 5:
            return Space.Empty
        return seat

    def count(self, space):
        return sum(sum(c == space for c in col) for col in self.seats)

    def __str__(self):
        return "\n".join("".join({Space.Floor: ".", Space.Empty: "L", Space.Occupied: "#"}.get(c) for c in col) for col in self.seats)




def test():
    small = """L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL"""
    s = Seats(small)
    while s.step(version=1):
        print(s)
    print(s.count(Space.Occupied))


def part_1() -> str:
    s = Seats(puzzle)
    while s.step(version=1):
        pass
    return str(s.count(Space.Occupied))


def part_2() -> str:
    s = Seats(puzzle)
    while s.step(version=2):
        pass
    return str(s.count(Space.Occupied))


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
