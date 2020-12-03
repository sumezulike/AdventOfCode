from puzzles import day1 as puzzle

puzzle = [int(x) for x in puzzle.split("\n")]

def part_1():
    for x in puzzle:
        for y in puzzle:
            if x + y == 2020:
                print(x*y)
                return

def part_2():
    for x in puzzle:
        for y in puzzle:
            for z in puzzle:
                if x + y + z == 2020:
                    print(x*y*z)
                    return

if __name__ == '__main__':
    print("Part 1:")
    part_1()
    print("Part 2:")
    part_2()
