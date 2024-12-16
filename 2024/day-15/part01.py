DIR = {
    ">": [0, 1],
    "^": [-1, 0],
    "<": [0, -1],
    "v": [1, 0],
}
PLAYER = "@"
EMPTY = "."
BOX = "O"
WALL = "#"


def read_file():
    board = []
    movements = []
    rx, ry = 0, 0

    with open("input-01.txt", "r") as file:
        for line in file:
            if line == "\n":
                break
            board.append(list(line.strip()))

            if PLAYER in board[-1]:
                rx = board[-1].index(PLAYER)
                ry = len(board) - 1
                board[-1][rx] = "."

        for line in file:
            movements += list(line.strip())

    return board, movements, rx, ry


def main():
    board, movements, rx, ry = read_file()
    movements.reverse()

    while movements:
        mov = movements.pop()
        my, mx = DIR[mov]
        nx, ny = rx + mx, ry + my
        if board[ny][nx] == EMPTY:
            rx, ry = nx, ny
        elif board[ny][nx] == BOX:
            while board[ny][nx] == BOX:
                nx, ny = nx + mx, ny + my
            if board[ny][nx] == EMPTY:  # Move everything one cell
                board[ny][nx] = BOX
                rx, ry = rx + mx, ry + my
                board[ry][rx] = EMPTY

    res = 0
    for y, line in enumerate(board):
        for x, cell in enumerate(line):
            if cell == BOX:
                res += y * 100 + x
    return res


if __name__ == "__main__":
    print(f"{main()}")  # 1430439
