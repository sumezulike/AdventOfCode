from functools import partial

from puzzles import day7 as puzzle

def parse_puzzle(p: str) -> list[int]:
    return [int(x) for x in p.split(",")]

def get_fuel_costs_linear(positions: list[int], target: int) -> int:
    return sum(abs(i-target) for i in positions)

def get_fuel_costs_sums(positions: list[int], target: int) -> int:
    sum_n = lambda n: (n+1)*n // 2
    return sum(sum_n(abs(i-target)) for i in positions)

def find_min_cost(positions: list[int], cost_func: callable) -> tuple[int, int]:
    f = partial(cost_func, positions)
    return min([(x, f(x)) for x in range(min(positions), max(positions))], key=lambda m: m[1])

def test():
    test_puzzle = "16,1,2,0,4,2,7,1,2,14"
    print(find_min_cost(parse_puzzle(test_puzzle), cost_func=get_fuel_costs_linear))
    print(find_min_cost(parse_puzzle(test_puzzle), cost_func=get_fuel_costs_sums))

def part_1() -> str:
    return str(find_min_cost(parse_puzzle(puzzle), cost_func=get_fuel_costs_linear))

def part_2() -> str:
    return str(find_min_cost(parse_puzzle(puzzle), cost_func=get_fuel_costs_sums))


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
