from itertools import combinations
from utils import read_file


def main():
    nodes, r, c = read_file()
    new_ant = set()

    def calc_antinode(a, b):
        antis = set()
        (ax, ay) = a
        (bx, by) = b
        dx = bx - ax
        dy = by - ay

        cx, cy = ax - dx, ay - dy
        if is_in_bounds(cx, cy):
            antis.add((cx, cy))
        cx, cy = bx + dx, by + dy
        if is_in_bounds(cx, cy):
            antis.add((cx, cy))

        return antis

    def is_in_bounds(x, y):
        return 0 <= x < c and 0 <= y < r

    for freq in nodes:
        nodes_freq = nodes[freq]
        for a, b in combinations(nodes_freq, r=2):
            new_ant |= calc_antinode(a, b)
    return len(new_ant)


if __name__ == "__main__":
    print(f"{main()}")  # 381
