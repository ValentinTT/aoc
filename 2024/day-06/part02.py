from utils import *

def main():
    board, gx, gy, direction = read_file()
    start_x, start_y, start_direction = gx, gy, direction
    r, c = len(board), len(board[0])

    visited_cord = set()
    # visited_cord.add(gx, gy) It cant be placed at the start (unless it pass more than once)
    while True:
        dx, dy = DIRECTIONS[direction]
        nx, ny = gx + dx, gy + dy
        if nx < 0 or nx >= c or ny < 0 or ny >= r:  ## out
            break
        if board[ny][nx] == BLOCK:
            direction = (direction + 1) % len(DIRECTIONS)
            continue
        if (nx, ny) not in visited_cord:
            visited_cord.add((nx, ny))
        gx, gy = nx, ny

    def check_possible_loop(x, y):
        if board[y][x] == BLOCK:
            return False

        board[y][x] = BLOCK
        visited = set()
        visited.add((start_x, start_y, start_direction))
        gx, gy, direction = start_x, start_y, start_direction

        while True:
            dx, dy = DIRECTIONS[direction]
            nx, ny = gx + dx, gy + dy
            if nx < 0 or nx >= c or ny < 0 or ny >= r:  ## out
                board[y][x] = EMPTY
                return False
            if board[ny][nx] == BLOCK:
                direction = (direction + 1) % len(DIRECTIONS)
                continue
            if (nx, ny, direction) not in visited:
                visited.add((nx, ny, direction))
            else:
                board[y][x] = EMPTY
                return True
            gx, gy = nx, ny

    loop_portal_counter = 0

    for x, y in visited_cord:
        loop_portal_counter += check_possible_loop(x, y)

    return loop_portal_counter


if __name__ == "__main__":
    print(f"{main()}")  # 1503
