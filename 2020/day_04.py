from puzzles import day4 as puzzle


def parse_passports() -> list[dict]:
    passports = [
        {d.split(":")[0]: d.split(":")[1] for d in line.split()} for line in
        [batch.replace("\n", " ") for batch in puzzle.split("\n\n")]
    ]
    return passports


def find_missing_fields(passport: dict) -> list:
    all_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    return list(filter(lambda k: k not in passport.keys(), all_fields))


def part_1():
    passports = parse_passports()
    valid = [p for p in passports if not (m := find_missing_fields(p)) or m == ["cid"]]
    print(len(valid))


if __name__ == '__main__':
    print("Part 1:")
    part_1()
