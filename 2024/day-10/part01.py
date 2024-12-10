from utils import read_file, DIRECTIONS


def main():
    data = read_file()
    r = len(data)
    c = len(data[0])

    def in_grid(i, j):
        return (0 <= i < r) and (0 <= j < c)

    def find_paths(i, j):
        if data[i][j] != 0:
            return 0

        acc = 0
        stack = [(i, j)]
        visited = set()
        while len(stack) > 0:
            cy, cx = stack.pop()

            if data[cy][cx] == 9 and (cy, cx) not in visited:
                acc += 1
                visited.add((cy, cx))
                continue

            for dy, dx in DIRECTIONS:
                nx, ny = cx + dx, cy + dy
                if not in_grid(ny, nx):
                    continue
                if data[ny][nx] != data[cy][cx] + 1:
                    continue

                stack.append((ny, nx))
        return acc

    total = 0
    for i in range(r):
        for j in range(c):
            total += find_paths(i, j)
    return total


if __name__ == "__main__":
    print(f"{main()}")  # 574
