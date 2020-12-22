from pprint import pprint

from puzzles import day22 as puzzle

TAB = " "*4

def parse_input(decks: str) -> tuple[list[int], list[int]]:
    p1, p2 = decks.split("\n\n")
    p1, p2 = p1.split("\n")[1:], p2.split("\n")[1:]
    p1, p2 = [int(x) for x in p1], [int(x) for x in p2]
    return p1, p2


def play(p1: list[int], p2: list[int]) -> list[int]:
    i = 0
    while p1 and p2:
        i += 1
        print(f"-- Round {i} - -")
        print(f"Player 1's deck: {p1}")
        print(f"Player 2's deck: {p2}")
        play1 = p1[0]
        play2 = p2[0]
        p1, p2 = p1[1:], p2[1:]
        print(f"Player 1 plays: {play1}")
        print(f"Player 1 plays: {play2}")
        print(f"Player {1 if play1 > play2 else 2} wins the round!")
        if play1 > play2:
            p1 += [play1, play2]
        else:
            p2 += [play2, play1]
        print()
    return p1 or p2


def rplay(p1: list[int], p2: list[int], depth=0) -> tuple[int, list[int]]:
    i = 0
    history = set()
    print(f"{depth*TAB}-- Game {depth} - -")
    while p1 and p2:
        i += 1
        print(f"{depth*TAB}-- Round {i} - -")
        print(f"{depth*TAB}Player 1's deck: {p1}")
        print(f"{depth*TAB}Player 2's deck: {p2}")
        state = str((p1, p2))
        if state in history:
            print(f"{depth*TAB}RECURSION WARNING: PLAYER 1 WINS")
            return 1, p1
        history.add(state)
        play1 = p1[0]
        play2 = p2[0]
        p1, p2 = p1[1:], p2[1:]
        print(f"{depth*TAB}Player 1 plays: {play1}")
        print(f"{depth*TAB}Player 1 plays: {play2}")

        winner = 1 if play1 > play2 else 2

        if play1 <= len(p1) and play2 <= len(p2):
            print(f"{depth*TAB}HOLD MY CARDS, I'M GOING IN")
            winner, _ = rplay(p1[:play1], p2[:play2], depth=depth+1)

        print(f"{depth*TAB}Player {winner} wins the round!")
        if winner == 1:
            p1 += [play1, play2]
        else:
            p2 += [play2, play1]
        print()
    print(f"{depth*TAB}Player {1 if p1 else 2} wins game {depth}!")
    print()
    return (1, p1) if p1 else (2, p2)

def score(deck: list[int]):
    return sum((len(deck)-i)*x for i, x in enumerate(deck))

def test():
    te = """Player 1:\n9\n2\n6\n3\n1\n\nPlayer 2:\n5\n8\n4\n7\n10"""
    inf = """Player 1:\n43\n19\n\nPlayer 2:\n2\n29\n14"""
    p1, p2 = parse_input(te)
    rplay(p1, p2)

def part_1() -> str:
    p1, p2 = parse_input(puzzle)
    winner = play(p1, p2)
    return str(score(winner))

def part_2() -> str:
    p1, p2 = parse_input(puzzle)
    winner, deck = rplay(p1, p2)
    return str(score(deck))


if __name__ == '__main__':
    test()
    pprint("Part 1:")
    pprint(part_1())
    pprint("Part 2:")
    pprint(part_2())
