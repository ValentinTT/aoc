def read_file():
    data = []
    with open("input-01.txt", "r") as file:
        for line in file:
            data.append(list(map(int, list(line[:-1]))))
    return data


DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
