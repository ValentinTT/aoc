def read_file():
    left_list = []
    right_list = []

    with open("input-01.txt", "r") as f:
        for line in f:
            values = line.split()
            left_list.append(int(values[0]))
            right_list.append(int(values[1]))

    return left_list, right_list
