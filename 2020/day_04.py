import re
from puzzles import day4 as puzzle

from tests import day4 as tests


def parse_passports(data) -> list[dict]:
    passports = [
        {d.split(":")[0]: d.split(":")[1] for d in line.split()} for line in
        [batch.replace("\n", " ") for batch in data.split("\n\n")]
    ]
    return passports


def find_missing_fields(passport: dict) -> list:
    all_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    return list(filter(lambda k: k not in passport.keys(), all_fields))


def part_1(data=puzzle):
    passports = parse_passports(data)
    valid = [p for p in passports if not (m := find_missing_fields(p)) or m == ["cid"]]
    print(len(valid))


def part_2(data=puzzle):
    passports = parse_passports(data)

    def is_valid(p):
        missing = find_missing_fields(p)
        if missing and missing != ["cid"]:
            return False
        if len(p["byr"] + p["iyr"] + p["eyr"]) != 3 * 4:
            return False
        if not 1920 <= int(p["byr"]) <= 2002:
            return False
        if not 2010 <= int(p["iyr"]) <= 2020:
            return False
        if not 2020 <= int(p["eyr"]) <= 2030:
            return False
        if len(p["hgt"]) < 4:
            return False
        height, unit = int(p["hgt"][:-2]), p["hgt"][-2:]
        if unit not in ["cm", "in"]:
            return False
        if unit == "cm":
            if not 150 <= height <= 193:
                return False
        elif unit == "in":
            if not 59 <= height <= 76:
                return False
        if not re.match(r"#[0-9a-f]{6}", p["hcl"]):
            return False
        if not p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        if not re.match(r"\d{9}\b", p["pid"]):
            return False
        return True

    valid = [p for p in passports if is_valid(p)]
    print(len(valid))

if __name__ == '__main__':
    print("Part 1:")
    part_1()
    print("Part 2:")
    part_2()
