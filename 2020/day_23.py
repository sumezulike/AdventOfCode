from puzzles import day23 as puzzle


def move_cups(cups: list[int], current_label: int) -> tuple[list[int], int]:
    current = cups.index(current_label)
    print(" ".join(f"({c})" if c == current_label else str(c) for c in cups))
    head, chosen, tail = cups[:current + 1], cups[current + 1: current + 4], cups[current + 4:]
    print(f"Pick up: {chosen}")
    rest = head + tail
    dest_label = int(current_label) - 1
    while dest_label not in rest:
        dest_label -= 1
        if dest_label < min(cups):
            dest_label = max(cups)
    dest = rest.index(dest_label)
    print(f"Destination: {dest_label}")
    moved = rest[:dest + 1] + chosen + rest[dest + 1:]
    moved = moved[current:] + moved[:current]

    current = moved.index(current_label)
    print(" ".join(f"({c})" if c == current_label else str(c) for c in moved))
    print()
    return moved, moved[(current + 1) % len(moved)]


def test():
    cups = [int(i) for i in "389125467"]
    c = cups[0]
    for i in range(100):
        cups, c = move_cups(cups, c)
        print(cups)


def part_1() -> str:
    cups = [int(i) for i in puzzle]
    c = cups[0]
    for i in range(100):
        cups, c = move_cups(cups, c)
    one = cups.index(1)
    return "".join(str(x) for x in cups[one + 1:] + cups[:one])


def part_2() -> str:
    #942387615
    cups = [int(i) for i in puzzle] + list(range(int(max(puzzle)), 1000000 + 1))
    c = cups[0]
    for i in range(10):
        cups, c = move_cups(cups, c)
    one = cups.index(1)
    return (a := cups[one + 1]), (b := cups[one + 2]), a * b


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
