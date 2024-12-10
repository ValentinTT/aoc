from collections import defaultdict


def read_file():
    board = defaultdict(list)
    r, c = 0, 0
    with open("input-01.txt", "r") as file:
        for line in file:
            for x, c in enumerate(list(line[:-1])):
                if c != ".":
                    board[c].append((x, r))
            c = len(line)
            r += 1
    return board, r, c
