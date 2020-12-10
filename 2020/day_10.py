import itertools
from math import prod

from puzzles import day10 as puzzle


def test():
    test_input = "28\n33\n18\n42\n31\n14\n46\n20\n48\n47\n24\n23\n49\n45\n19\n38\n39\n11\n1\n32\n25\n35\n8\n17\n7\n9\n4\n2\n34\n10\n3"
    small_test = "16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4"
    special_test = "1\n2\n3\n"  # "1\n4\n5\n6\n7\n8\n11\n12\n13\n14\n16\n17"
    n = parse_adapters(test_input)
    print("Is valid", is_valid(n))
    o = count_diffs(n, 1)
    print(o, "(22)")
    t = count_diffs(n, 3)
    print(t, "(10)")

    c = count_combinations(n)
    print(c, "(19208)")

    n = parse_adapters(small_test)
    print("Is valid", is_valid(n))
    c = count_combinations(n)
    print(c, "(8)")

    n = parse_adapters(special_test)
    print("Valid:", is_valid(n))
    c = count_combinations(n)
    print(c, "(?)")


def parse_adapters(adapters: str = puzzle) -> list[int]:
    return sorted((m := [int(i) for i in adapters.split()]) + [0, max(m) + 3])


def count_diffs(numbers: list[int], diff: int) -> int:
    d = [numbers[i - 1] == numbers[i] - diff for i in range(1, len(numbers))]
    return sum(d)


def count_combinations(numbers: list[int]):
    """
    (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)

    (0), 1, 4,    6, 7, 10, 11, 12, 15, 16, 19, (22)
    (0), 1, 4,    6, 7, 10,     12, 15, 16, 19, (22)
    (0), 1, 4,       7, 10, 11, 12, 15, 16, 19, (22)

    (0), 1, 4, 5,    7, 10, 11, 12, 15, 16, 19, (22)
    (0), 1, 4, 5,    7, 10,     12, 15, 16, 19, (22)
    (0), 1, 4,       7, 10, 11, 12, 15, 16, 19, (22)

    (0), 1, 4, 5, 6, 7, 10,     12, 15, 16, 19, (22)
    (0), 1, 4, 5,    7, 10,     12, 15, 16, 19, (22)
    (0), 1, 4,    6, 7, 10,     12, 15, 16, 19, (22)

    (0), 1, 4,       7, 10,     12, 15, 16, 19, (22)

    """
    # s = list(filter(lambda x: x, [sum(i < x < i + 3 for x in numbers) for i in numbers]))
    # x = prod(s)
    # u = {numbers[i]: numbers[i + 1] - numbers[i - 1] <= 3 for i in range(1, len(numbers) - 1)}
    # r = {numbers[i]: sum(numbers[i] + e in numbers for e in [-2, -1, 1, 2]) if numbers[i - 1] + 3 > numbers[i] > numbers[i + 1] - 3 else 0 for i in range(1, len(numbers))}
    #
    # v = [numbers[i] for i in range(1, len(numbers) - 1) if numbers[i + 1] - numbers[i - 1] <= 3]
    # v2 = [3]+[max(numbers[i+1]-numbers[i], -(numbers[i-1]-numbers[i])) for i in range(1, len(numbers) - 1)]+[3]
    #
    # v30 = [0 if x == 3 else x for x in v2]
    #
    # vals = {i: j for i, j in zip(numbers, v30)}
    # perms = [{numbers.index(v[i]): list(p)[i] for i in range(len(v))} for p in itertools.product([0, 1], repeat=len(v))]
    # count = 0
    # for p in perms:
    #     c = 0
    #     for n, v in vals.items():
    #         if n in p:
    #             c += v
    #         else:
    #             c = 0
    #         if c >= 3:
    #             break
    #     count += 1


    shards = [[0]]
    for i, x in enumerate(numbers[1:]):
        if x > numbers[i] + 2:
            shards.append([x])
        else:
            shards[-1].append(x)
    shards = [s for s in shards if len(s) > 1]
    combs = []
    for s in shards:
        var = s[1:-1]
        perms = [list(i) for i in itertools.product([0, 1], repeat=len(var))]
        z = [list(zip(var, p)) for p in perms]
        t = [[a[0] for a in x if a[1]] for x in z]
        combs.append(sum(is_valid([s[0]]+ts+[s[-1]]) for ts in t))
    return prod(combs)

def is_valid(nums: list[int]) -> bool:
    return all(nums[i] >= nums[i + 1] - 3 for i in range(len(nums) - 1))


def part_1() -> str:
    nums = parse_adapters()
    ones = count_diffs(nums, 1)
    threes = count_diffs(nums, 3)
    return f"{ones * threes}"


def part_2() -> str:
    nums = parse_adapters()
    c = count_combinations(nums)
    return str(c)


if __name__ == '__main__':
    test()
    print("Part 1:")
    print(part_1())
    print("Part 2:")
    print(part_2())
