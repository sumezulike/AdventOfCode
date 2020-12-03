from .puzzles import day1 as puzzle

puzzle = [int(x) for x in puzzle.split("\n")]

def part_1():
    for x in puzzle:
        for y in puzzle:
            if x + y == 2020:
                print(x*y)

def part_2():
    for x in puzzle:
        for y in puzzle:
            for z in puzzle:
                if x + y + z == 2020:
                    print(x*y*z)

if __name__ == '__main__':
    part_2()
