from puzzles import day8 as puzzle


def test():
    process_code()


def process_code(code: str = puzzle) -> tuple[bool, int]:
    code = code.split("\n")
    ip = 0
    acc = 0
    history = set()
    while True:
        if ip >= len(code):
            return True, acc
        if ip in history:
            return False, acc
        else:
            history.add(ip)
        instr, param = code[ip].split()
        if instr == "nop":
            ip += 1
        elif instr == "acc":
            acc += int(param)
            ip += 1
        elif instr == "jmp":
            ip += int(param)
        else:
            raise Exception(f"Unknown instruction: {instr}")


def bruteforce_code_changes(find, sub, code=puzzle):
    pos = 0
    for i in range(code.count(find)):
        pos += code[pos + len(find):].find(find) + len(find)
        repl = code[:pos] + code[pos:].replace(find, sub, 1)
        yield repl


def part_1() -> str:
    return str(process_code()[1])


def part_2() -> str:
    for code in bruteforce_code_changes("nop", "jmp", code=puzzle):
        term, res = process_code(code)
        if term:
            return str(res)
    for code in bruteforce_code_changes("jmp", "nop", code=puzzle):
        term, res = process_code(code)
        if term:
            return str(res)


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
