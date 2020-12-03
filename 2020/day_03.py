import math
from typing import List

from puzzles import day3 as puzzle


def is_blocked(fields: List[str], x: int, y: int) -> bool:
    x %= len(fields[0])
    return fields[y][x] == "#"


def count_trees(x_step, y_step):
    fields = puzzle.split("\n")
    return len([row for i, row in enumerate(fields[::y_step]) if is_blocked(fields, x=i * x_step, y=i * y_step)])


def part_1():
    print(count_trees(3, 1))


def part_2():
    counts = [
        count_trees(1, 1),
        count_trees(3, 1),
        count_trees(5, 1),
        count_trees(7, 1),
        count_trees(1, 2),
    ]
    print(math.prod(counts))


if __name__ == '__main__':
    print("Part 1:")
    part_1()
    print("Part 2:")
    part_2()
