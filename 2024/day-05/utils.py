def read_file():
    ordering_rules = {}
    updates = []

    with open("input-01.txt", "r") as file:
        for line in file:
            if line == "\n":
                break
            first, second = list(map(int, line.split("|")))
            if first not in ordering_rules:
                ordering_rules[first] = set()
            ordering_rules[first].add(second)
        for line in file:
            updates.append(list(map(int, line.split(","))))
    return ordering_rules, updates
