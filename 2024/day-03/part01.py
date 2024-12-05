def read_file():
    data = ""
    with open("input-01.txt", "r") as file:
        for line in file:
            data += line
    return data


def main():
    corrupted = read_file()
    corrupted += "//////"

    def get_number(i):
        number = 0
        while i < len(corrupted):
            if corrupted[i].isdigit():
                number = number * 10 + int(corrupted[i])
                i += 1
            else:
                break
        if number < 1 or number > 999:
            return -1, i
        return number, i

    total = 0
    for i in range(len(corrupted) - 6):
        if corrupted[i : i + 4] != "mul(":
            continue
        x, i = get_number(i + 4)
        if corrupted[i] != "," or x == -1:
            continue
        y, i = get_number(i + 1)
        if corrupted[i] != ")" or y == -1:
            continue
        total += x * y

    return total


if __name__ == "__main__":
    print(f"result: {main()}")  # 182619815
