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
    finish_coord = [[0] * c for i in range(r)]
    qs = [0] * 4

    for robot in robots:
        (x, y), (vx, vy) = robot
        x = (x + 100 * vx) % c
        y = (y + 100 * vy) % r
        finish_coord[y][x] += 1
        if y < r // 2 and x < c // 2:
            qs[0] += 1
        elif y < r // 2 and x > c // 2:
            qs[1] += 1
        elif y > r // 2 and x < c // 2:
            qs[2] += 1
        elif y > r // 2 and x > c // 2:
            qs[3] += 1

    res = qs[0]
    for q in qs[1:]:
        res *= q
    return res


if __name__ == "__main__":
    print(f"{main()}")  # 230686500
