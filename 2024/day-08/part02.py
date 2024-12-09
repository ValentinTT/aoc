from collections import defaultdict
from itertools import combinations


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


def main():
    nodes, r, c = read_file()
    new_ant = set()

    def calc_antinode(a, b):
        antis = set()
        (ax, ay) = a
        (bx, by) = b
        dx = bx - ax
        dy = by - ay

        for i in range(r):
            cx, cy = ax - dx * i, ay - dy * i
            if is_in_bounds(cx, cy):
                antis.add((cx, cy))
            else:
                break
        for i in range(r):
            cx, cy = bx + dx * i, by + dy * i
            if is_in_bounds(cx, cy):
                antis.add((cx, cy))
            else:
                break

        return antis

    def is_in_bounds(x, y):
        return 0 <= x < c and 0 <= y < r

    for freq in nodes:
        nodes_freq = nodes[freq]
        for a, b in combinations(nodes_freq, r=2):
            new_ant |= calc_antinode(a, b)
    return len(new_ant)


if __name__ == "__main__":
    print(f"{main()}")  # 1184
