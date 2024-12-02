def read_file():
    reports = []

    with open("input-01.txt", "r") as f:
        for line in f:
            reports.append(list(map(int, line.split())))

    return reports