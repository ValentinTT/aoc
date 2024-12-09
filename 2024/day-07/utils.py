def read_file():
    data = []
    with open("input-01.txt", "r") as file:
        for line in file:
            aux = line.strip().split(": ")
            res = aux[0]
            op = aux[1].split(" ")
            data.append((res, op))
    return data
