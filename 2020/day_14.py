from pprint import pprint
from itertools import product
from puzzles import day14 as puzzle
import re

def parse_input(masks :str) -> list[tuple[str, list[list[int]]]]:
    return list((mask, [re.findall(r"\d+", n) for n in numbers if re.findall(r"\d+", n)]) for mask, *numbers in [block.split("\n") for block in masks.split("mask = ")[1:]])

def work_numbers(nums):
    data = {}
    for mask, numbers in nums:
        ones_mask = "".join("1" if c == "1" else "0" for c in mask)
        zeroes_mask = "".join("0" if c == "0" else "1" for c in mask)
        for index, num in numbers:
            res = (int(num) | int(ones_mask, 2) )& int(zeroes_mask, 2)
            data[int(index)] = res
    return data

def quantum_work_numbers(nums: list[tuple[str, list[list[int]]]]):
    data = {}
    for mask, numbers in nums:
        vars = list(product([0, 1], repeat=mask.count("X")))
        masks = []
        for v in vars:
            m = "".join("_" if c != "X" else "X" for c in mask)
            for i in v:
                m = m.replace("X", str(i), 1)
            masks.append(m)
        for m in masks:
            z_m = int("".join("0" if c == "0" else "1" for c in m), 2)
            o_m = int("".join("1" if c == "1" else "0" for c in m), 2)
            for index, num in numbers:
                pos = int(index) | int(mask.replace("X", "0"), 2)
                pos = (pos | o_m) & z_m
                data[pos] = int(num)
    return data

def test():
    test = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
    nums = parse_input(test)
    d = work_numbers(nums)
    print(sum(d.values()))
    qtest = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
    qnums = parse_input(qtest)
    qd = quantum_work_numbers(qnums)
    print(sum(qd.values()))

def part_1() -> str:
    nums = parse_input(puzzle)
    d = work_numbers(nums)
    return sum(d.values())

def part_2() -> str:
    nums = parse_input(puzzle)
    d = quantum_work_numbers(nums)
    return sum(d.values())


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
