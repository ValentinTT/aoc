EMPTY = "."
BLOCK = "#"
VISITED = "X"
GUARD = ["v", ">", "^", "<"]
DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def read_file():
    board = []
    gx, gy = -1, -1
    direction = None

    with open("input-01.txt", "r") as file:
        for line in file:
            board.append(list(line[:-1]))
            s = set(board[-1])
            if len(s) != 3:  # There is no guard
                continue
            s.discard(EMPTY)
            s.discard(BLOCK)
            guard = list(s)[0]
            gx = line.find(guard)
            gy = len(board) - 1
            direction = GUARD.index(guard)
            board[gy][gy] = VISITED

    return board, gx, gy, direction
