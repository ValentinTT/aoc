def read_file():
    with open("input-01.txt", "r") as file:
        data = list(map(int, file.read().strip().split(" ")))
    return data


def blink(arr):
    new_arr = []

    for stone in arr:
        new_arr += proccess_stone(stone)

    return new_arr


def proccess_stone(stone):
    if stone == 0:
        return [1]

    n = str(stone)
    if len(n) % 2 == 0:
        half = len(n) // 2
        return [int(n[0:half]), int(n[half:])]
    return [stone * 2024]


def main(n):
    data = read_file()

    for _ in range(n):
        data = blink(data)
    return len(data)


if __name__ == "__main__":
    print(f"{main(25)}")  # 217812
