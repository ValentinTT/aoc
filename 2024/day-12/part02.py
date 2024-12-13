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

    def explore_region(i, j, region, borders):
        if (i, j) in visited:
            return region, borders
        visited.add((i, j))
        region_letter = board[i][j]

        for [dx, dy] in DIRECTIONS:
            nx, ny = dx + j, dy + i
            if not in_grid(nx, ny) or board[ny][nx] != region_letter:
                by, bx = i + dy / 2, j + dx / 2
                borders[(by, bx)] = (dy / 2, dx / 2)
                continue
            # next to the same region
            region.add((ny, nx))
            region, borders = explore_region(ny, nx, region, borders)
        return region, borders

    def count_sides(borders):
        seen = set()
        sides = 0
        for border, direction in borders.items():
            if border in seen: continue
            seen.add(border)
            sides += 1
            i, j = border
            if i % 1 == 0: # then this is what we need to increment or decrement
                for di in [-1, 1]:
                    aside = i + di, j
                    while borders.get(aside) == direction:
                        seen.add(aside)
                        aside = aside[0] + di, j
            else: # then this is what we need to increment or decrement
                for dj in [-1, 1]:
                    aside = i, j + dj
                    while borders.get(aside) == direction:
                        seen.add(aside)
                        aside = i, aside[1] + dj
                
        return sides

    for i in range(r):
        for j in range(c):
            if (i, j) not in visited:  # new region
                region, borders = explore_region(i, j, set([(i, j)]), {})
                total += len(region) * count_sides(borders)
    return total


if __name__ == "__main__":
    print(f"{main()}")  # 869070
