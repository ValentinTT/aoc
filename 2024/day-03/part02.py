def read_file():
    data = ""
    with open("input-01.txt", "r") as file:
        for line in file:
            data += line
    return data


def main():
    corrupted = read_file()
    corrupted += "//////"
    DO = "do()"
    DONT = "don't()"
    MUL = "mul("

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
    i = 0
    while i < len(corrupted) - 6:
        if corrupted[i : i + len(DONT)] == DONT:  ## Found a don't() skip until do()
            while i < len(corrupted) - len(DO):
                if corrupted[i : i + 4] == DO:
                    break
                i += 1
            if i >= len(corrupted) - len(DO):  ## skip to the end
                break

        if corrupted[i : i + len(DO)] != MUL:
            i += 1
            continue

        x, i = get_number(i + len(MUL))
        if corrupted[i] != "," or x == -1:
            i += 1
            continue
        y, i = get_number(i + 1)
        if corrupted[i] != ")" or y == -1:
            i += 1
            continue
        total += x * y
        i += 1

    return total


if __name__ == "__main__":
    print(f"result: {main()}")  # 80747545
