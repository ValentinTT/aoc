from utils import read_file


def main():
    ordering_rules, updates = read_file()

    def validate_update(update, i):
        first = update[i]
        if first not in ordering_rules:
            return False

        for j in range(i + 1, len(update)):
            second = update[j]
            if second not in ordering_rules[first]:
                return False
        return True

    res = 0

    for update in updates:
        is_ok = True
        for i in range(len(update) - 1):
            if not validate_update(update, i):
                is_ok = False
                break
        if is_ok:
            res += update[len(update) // 2]
    return res


if __name__ == "__main__":
    print(f"corrects update middle sum: {main()}")  # 6498
