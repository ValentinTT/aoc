from utils import *


def main():
    # I don't check if there is trap so far.
    # (I need instead of mark each cell as visited, mark each cell in for aspect
    # [visited up, down, left, right] and if one is repeated I'm in a loop)
    board, gx, gy, direction = read_file()
    r, c = len(board), len(board[0])

    visited_counter = 0
    while True:
        dx, dy = DIRECTIONS[direction]
        nx, ny = gx + dx, gy + dy
        if nx < 0 or nx >= c or ny < 0 or ny >= r:  ## out
            break
        if board[ny][nx] == BLOCK:
            direction = (direction + 1) % len(DIRECTIONS)
            continue
        if board[ny][nx] == EMPTY:
            visited_counter += 1
            board[ny][nx] = VISITED
        gx, gy = nx, ny

    return visited_counter + 1


if __name__ == "__main__":
    print(f"{main()}")  # 4454
