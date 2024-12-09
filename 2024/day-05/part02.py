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
        i = 0
        is_ok = True
        while i < len(update) - 1:
            if not validate_update(update, i):
                update = update[0:i] + update[i + 1 :] + [update[i]]
                is_ok = False
            else:
                i += 1
        if not is_ok:
            print(update)
            res += update[len(update) // 2]
    return res


if __name__ == "__main__":
    print(f"incorrect update middle sum after sorting: {main()}")  # 5017
