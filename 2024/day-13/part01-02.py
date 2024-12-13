def read_file():
    prizes = []
    with open("input-01.txt", "r") as file:
        prize = []
        for line in file:
            if line[0] == "B":
                x, y = line[12:].strip().split(", ")
                x, y = int(x), int(y[1:])
                prize.append((x, y))
            elif line[0] == "P":
                x, y = line[9:].strip().split(", ")
                x, y = int(x), int(y[2:])
                prizes.append([x, y, prize])
                prize = []
    return prizes


def main(plusx=0, plusy=0):
    prizes = read_file()
    total = 0

    for prize in prizes:
        px, py, [(ax, ay), (bx, by)] = prize
        px += plusx
        py += plusy
        ca = (px * by - py * bx) / (ax * by - ay * bx)
        cb = (px - ax * ca) / bx
        if ca % 1 == cb % 1 == 0:
            total += ca * 3 + cb
    return int(total)


if __name__ == "__main__":
    print(f"part 1: {main()}")  # 29522
    print(f"part 2: {main(10000000000000, 10000000000000)}")  # 101214869433312
