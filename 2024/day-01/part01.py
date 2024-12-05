from utils import read_file


def main():
    l, r = read_file()
    l.sort()
    r.sort()
    total = 0

    for a, b in zip(l, r):
        total += abs(a - b)
    return total


if __name__ == "__main__":
    print(f"total distance {main()}")  # 2176849
