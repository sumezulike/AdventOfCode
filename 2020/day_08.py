from puzzles import day8 as puzzle


def test():
    p = Processor()
    p.process_code(puzzle)


class Processor:

    def __init__(self):
        self.ip = 0
        self.acc = 0
        self.history = set()
        self.code = []

        self.code_table = {
            "nop": self.__nop,
            "acc": self.__acc,
            "jmp": self.__jmp
        }


    def reset(self, code):
        self.ip = 0
        self.acc = 0
        self.history = set()
        self.code = code.split("\n")


    def __acc(self, _param):
        self.acc += int(_param)
        self.ip += 1


    def __nop(self, _param):
        self.ip += 1


    def __jmp(self, _param):
        self.ip += int(_param)


    def __unkn(self, *args, **kwargs):
        raise Exception(f"Unknown instruction: '{self.code[self.ip]}', {args, kwargs}")


    def process_code(self, code: str = puzzle) -> tuple[bool, int]:
        self.reset(code)
        while self.ip not in self.history:
            if self.ip >= len(self.code):
                return True, self.acc
            self.history.add(self.ip)
            self.process_next_instruction()
        return False, self.acc


    def process_next_instruction(self):
        instr, param = self.code[self.ip].split(" ", 1)
        func = self.code_table.get(instr)
        if func:
            # noinspection PyArgumentList
            func(param)
        else:
            self.__unkn()


def bruteforce_code_changes(find, sub, code=puzzle):
    pos = 0
    for i in range(code.count(find)):
        pos += code[pos + len(find):].find(find) + len(find)
        repl = code[:pos] + code[pos:].replace(find, sub, 1)
        yield repl


def part_1() -> str:
    p = Processor()
    _, res = p.process_code(puzzle)
    return str(res)


def part_2() -> str:
    p = Processor()
    for code in bruteforce_code_changes("nop", "jmp", code=puzzle):
        term, res = p.process_code(code)
        if term:
            return str(res)
    for code in bruteforce_code_changes("jmp", "nop", code=puzzle):
        term, res = p.process_code(code)
        if term:
            return str(res)


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
