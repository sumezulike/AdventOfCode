from puzzles import day12 as puzzle

EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)
NORTH = (0, 1)

class Ship:

    def __init__(self, position: tuple = (0, 0)):
        self.position = position
        self.direction = EAST


    def run_route(self, directions: str):
        for d in directions.split("\n"):
            direc, dist = d[0], int(d[1:])
            if direc in "RL":
                self.turn(direc, dist)
            else:
                self.move(direc, dist)


    def move(self, direc: str, dist: int):
        d = {"E": EAST, "S": SOUTH, "W": WEST, "N": NORTH, "F": self.direction}.get(direc)
        self.position = self.position[0] + dist * d[0], self.position[1] + dist * d[1]


    def turn(self, direc: str, dist: int):
        dirs = [EAST, SOUTH, WEST, NORTH]
        assert dist % 90 == 0
        turns = dist // 90
        if direc == "R":
            self.direction = dirs[(dirs.index(self.direction) + turns) % len(dirs)]
        elif direc == "L":
            self.direction = dirs[(dirs.index(self.direction) - turns) % len(dirs)]
        else:
            raise Exception("Wrong turn")

class Waypoint:
    def __init__(self, position: tuple):
        self.position = position

    def move(self, direc: str, dist: int):
        d = {"E": EAST, "S": SOUTH, "W": WEST, "N": NORTH}.get(direc)
        self.position = self.position[0] + dist * d[0], self.position[1] + dist * d[1]

    def turn(self, direc: str, dist: int):
        assert dist % 90 == 0
        turns = dist // 90
        for i in range(turns):
            if direc == "R":
                self.position = self.position[1], -1 * self.position[0]
            elif direc == "L":
                self.position = -1 * self.position[1], self.position[0]
            else:
                raise Exception("Wrong turn")


class WaypointShip:

    def __init__(self, position: tuple = (0, 0)):
        self.position = position
        self.waypoint = Waypoint(position=(10, 1))

    def run_route(self, directions: str):
        for d in directions.split("\n"):
            direc, dist = d[0], int(d[1:])
            if direc in "RL":
                self.waypoint.turn(direc, dist)
            elif direc == "F":
                self.move(dist)
            else:
                self.waypoint.move(direc, dist)


    def move(self, dist: int):
        self.position = self.position[0] + dist * self.waypoint.position[0], self.position[1] + dist * self.waypoint.position[1]



def man_dist(delta_x, delta_y) -> int:
    return abs(delta_x) + abs(delta_y)


def test():
    tiny = "F10\nN3\nF7\nR90\nF11"
    full = "W1\nF1\nE1\nF1\nN1\nF1\nS1\nF1\nR90\nR180\nR270\nR360\nR450\nL90\nL180\nL270\nL360\nL450"
    s = Ship()
    s.run_route(tiny)
    print(man_dist(*s.position), "(25)")
    ws = WaypointShip()
    ws.run_route(tiny)
    print(man_dist(*ws.position), "(286)")
    ws2 = WaypointShip()
    ws2.run_route(full)


def part_1() -> str:
    s = Ship()
    s.run_route(puzzle)
    return str(man_dist(*s.position))


def part_2() -> str:
    s = WaypointShip()
    s.run_route(puzzle)
    return str(man_dist(*s.position))


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
