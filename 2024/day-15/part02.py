DIR = {
    ">": [0, 1],
    "^": [-1, 0],
    "<": [0, -1],
    "v": [1, 0],
}
UP_OR_DOWN = ["v", "^"]
PLAYER = "@"
EMPTY = "."
BOX = "O"
BOX_L = "["
BOX_R = "]"
WALL = "#"


def read_file():
    board = []
    movements = []
    rx, ry = 0, 0

    with open("input-01.txt", "r") as file:
        for line in file:
            if line == "\n":
                break
            aux = []
            for c in line[:-1]:
                if c == BOX:
                    aux += [BOX_L, BOX_R]
                elif c == PLAYER:
                    rx = len(aux)
                    ry = len(board)
                    aux += [EMPTY, EMPTY]
                else:
                    aux += [c, c]
            board.append(aux)

        for line in file:
            movements += list(line.strip())

    return board, movements, rx, ry


def print_board(board):
    for line in board:
        print("".join(line))


def main():
    board, movements, rx, ry = read_file()
    movements.reverse()

    print("=" * len(board[0]))
    print("Initial board")
    print_board(board)

    def check_move(y, x, dy):
        cell = board[y][x]
        if cell == WALL:
            return [], False
        if cell == EMPTY:
            return [], True
        if cell == BOX_R:
            x -= 1  # Position in the left side of the box to start search
        cords_to_move_l, can_move_l = check_move(y + dy, x, dy)
        if not can_move_l:
            return [], False
        cords_to_move_r, can_move_r = check_move(y + dy, x + 1, dy)
        if not can_move_r:
            return [], False
        return [(y, x), (y, x + 1)] + cords_to_move_l + cords_to_move_r, True

    while movements:
        mov = movements.pop()
        my, mx = DIR[mov]
        nx, ny = rx + mx, ry + my

        cell = board[ny][nx]
        if cell == EMPTY:
            rx, ry = nx, ny
            continue
        elif cell == WALL:
            continue
        # Box
        if mov in UP_OR_DOWN:
            if cell == BOX_R:
                nx -= 1  # Position in the left side of the box to start search

            cords_to_move_a, can_move = check_move(ny, nx, my)
            if not can_move:
                continue

            cords_to_move_b, can_move = check_move(ny, nx + 1, my)
            if not can_move:
                continue

            cords_to_move = list(set(cords_to_move_a + cords_to_move_b))
            cords_to_move.sort()
            if my > 0:  # Make sure the first elements are the furthest from robot
                cords_to_move.reverse()

            for y, x in cords_to_move:
                board[y + my][x] = board[y][x]
                board[y][x] = "."
            ry = ry + my  # Only update y coord
        else:  # Moving left or right pushing a box
            while board[ny][nx] in [BOX_L, BOX_R]:
                nx, ny = nx + mx, ny + my
            # There is a wall stoping, don't move
            if board[ny][nx] == WALL:
                continue
            # There is space at the other end, move all boxes
            px = nx
            while px != rx:
                board[ry][px] = board[ry][px - mx]
                px = px - mx
            rx = rx + mx  # Only update x coordinate

    print("=" * len(board[0]))
    print("Final board")
    print_board(board)
    print("=" * len(board[0]))

    res = 0
    for y, line in enumerate(board):
        for x, cell in enumerate(line):
            if cell == BOX_L:
                res += y * 100 + x
    return res


if __name__ == "__main__":
    print(f"Result: {main()}")  # 1458740
