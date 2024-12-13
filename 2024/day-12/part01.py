DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def create_in_grid(r, c):
    return lambda x, y: 0 <= x < c and 0 <= y < r


def read_file():
    board = []
    with open("input-01.txt", "r") as file:
        for line in file:
            board.append(list(line.strip()))
    return board


def main():
    board = read_file()
    r, c = len(board), len(board[0])
    in_grid = create_in_grid(r, c)
    visited = set()
    total = 0

    def explore_region(i, j):  # returns area, perimeter
        if (i, j) in visited:
            return 0, 0
        visited.add((i, j))
        region_letter = board[i][j]
        area = 1
        perimeter = 4
        for [dx, dy] in DIRECTIONS:
            nx, ny = dx + j, dy + i
            if not in_grid(nx, ny):  # out of bounds
                continue
            r = board[ny][nx]
            if r != region_letter:  # next to another region
                continue
            # next to the same region
            a, p = explore_region(ny, nx)
            perimeter = perimeter - 1 + p
            area += a
        return area, perimeter

    for i in range(r):
        for j in range(c):
            if (i, j) not in visited:  # new region
                a, p = explore_region(i, j)
                total += a * p
    return total


if __name__ == "__main__":
    print(f"{main()}")  # 1431440
