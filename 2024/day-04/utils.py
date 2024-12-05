def read_file():
    data = ""
    with open("input-01.txt", "r") as file:
        data = file.read().strip().split("\n")
    return data
