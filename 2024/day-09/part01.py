def read_file():
    data = []
    with open("input-01.txt", "r") as file:
        compressed = file.read().strip()
        for i, c in enumerate(compressed):
            if i % 2 != 0:
                data += [-1] * int(c)
            else:
                data += [i // 2] * int(c)
    return data


def main():
    arr = read_file()
    print(arr)
    l, r = 0, len(arr) - 1
    while l < r:
        if arr[l] != -1:
            l += 1
            continue
        if arr[r] == -1:
            r -= 1
            continue
        arr[l] = arr[r]
        arr[r] = -1
        l += 1
        r -= 1

    total = 0
    for idx, id in enumerate(arr):
        if id == -1:
            break
        total += idx * id
    return total


if __name__ == "__main__":
    print(f"{main()}")  # 6519155389266
