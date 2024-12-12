def read_file():
    with open("input-01.txt", "r") as file:
        data = list(map(int, file.read().strip().split(" ")))
    return data


def main(n):
    data = read_file()

    cache = {}

    def stones_from_stone(stone, n):
        if (stone, n) in cache:
            return cache[(stone, n)]
        if n == 1:
            if len(str(stone)) % 2 == 0:
                return 2
            return 1
        stone_str = str(stone)
        if len(stone_str) % 2 == 0:
            half = len(stone_str) // 2
            a = stones_from_stone(int(stone_str[:half]), n - 1)
            b = stones_from_stone(int(stone_str[half:]), n - 1)
            cache[(stone, n)] = a + b
        elif stone == 0:
            a = stones_from_stone(1, n - 1)
            cache[(stone, n)] = a
        else:
            a = stones_from_stone(stone * 2024, n - 1)
            cache[(stone, n)] = a
        return cache[(stone, n)]

    res = 0
    for stone in data:
        res += stones_from_stone(stone, n)
    return res


if __name__ == "__main__":
    print(f"{main(75)}")  # 259112729857522
# Instead of calling 75 blink and iterating over lists with trillions of elements,
# stones_from_stone get called 171347 times
