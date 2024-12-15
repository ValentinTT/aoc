def read_file():
    robots = []
    with open("input-01.txt", "r") as file:
        for line in file:
            pos, vel = line[2:].strip().split(" v=")
            x, y = pos.split(",")
            vx, vy = vel.split(",")
            robots.append(((int(x), int(y)), (int(vx), int(vy))))
    return robots


def main():
    robots = read_file()
    r, c = 103, 101
    prev_pos = set()

    for j in range(10500):
        aux = [[0] * c for _ in range(r)]
        for i, robot in enumerate(robots):
            (x, y), (vx, vy) = robot
            x = (x + vx) % c
            y = (y + vy) % r
            aux[y][x] += 1
            robots[i] = (x, y), (vx, vy)
        s = ""
        for row in aux:
            s += "".join("#" if num != 0 else " " for num in row)
        if j > 7665 and j < 7678:
            print(j, "=" * 101)
            for row in aux:
                print("".join("#" if num != 0 else " " for num in row))
        if s in prev_pos:
            return j
        prev_pos.add(s)
    return -1


if __name__ == "__main__":
    print(f"{main()}")  # 7672
