from puzzles import day2 as puzzle

def parse_passwords() -> list:
    return [{"min": int(a.split("-")[0]), "max": int(a.split("-")[1]), "letter": b[0], "password": c} for a, b, c in [line.split() for line in puzzle.split("\n")]]

def part_1():
    passwords = parse_passwords()
    valid = [p["password"] for p in passwords if p["min"] <= p["password"].count(p["letter"]) <= p["max"]]
    print(len(valid))

def part_2():
    passwords = parse_passwords()
    valid = [p["password"] for p in passwords if (p["password"][p["min"]-1] + p["password"][p["max"]-1]).count(p["letter"]) == 1]
    print(len(valid))

if __name__ == '__main__':
    print("Part 1:")
    part_1()
    print("Part 2:")
    part_2()
