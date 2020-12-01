puzzle = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,13,23,1,23,10,27,1,13,27,31,2,31,10,35,1,35,9,39,1,39,13,43,1,13,43,47,1,47,13,51,1,13,51,55,1,5,55,59,2,10,59,63,1,9,63,67,1,6,67,71,2,71,13,75,2,75,13,79,1,79,9,83,2,83,10,87,1,9,87,91,1,6,91,95,1,95,10,99,1,99,13,103,1,13,103,107,2,13,107,111,1,111,9,115,2,115,10,119,1,119,5,123,1,123,2,127,1,127,5,0,99,2,14,0,0]
tests = [([1,0,0,0,99], [2,0,0,0,99]),
    ([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99])
]
PART2_RES = 19690720

def process_intcode(code: list):
    pointer = 0
    while code[pointer] != 99:
        if code[pointer] == 1:
            code[code[pointer + 3]] = code[code[pointer + 1]] + code[code[pointer + 2]]
        elif code[pointer] == 2:
            code[code[pointer + 3]] = code[code[pointer + 1]] * code[code[pointer + 2]]
        pointer += 4
    return code

def test():
    for t in tests:
        res = process_intcode(t[0])
        print("Passed" if res == t[1] else f"{res} should be {t[1]}")

def part_1():
    print(process_intcode(puzzle))

def part_2():
    for noun in range(99):
        for verb in range(99):
            temp = puzzle.copy()
            temp[1] = noun
            temp[2] = verb
            if process_intcode(temp)[0] == PART2_RES:
                return 100 * noun + verb

if __name__ == '__main__':
    print(part_2())
