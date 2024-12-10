SPACE = -1


def read_file():
    with open("input-01.txt", "r") as file:
        compact = file.read().strip()

    ubi = [0] * len(compact)
    sizes = [0] * len(compact)
    disk = []

    for i, c in enumerate(compact):
        size = int(c)
        if i % 2 == 0:  # file
            id = i // 2
            ubi[id] = len(disk)
            sizes[id] = size
            disk += [id] * size
        else:  # space
            disk += [SPACE] * size
    return ubi, sizes, disk


def main():
    ubi, sizes, disk = read_file()

    highest_id = 0
    for id in disk[::-1]:
        if id != SPACE:
            highest_id = id
            break

    for id_to_move in range(highest_id, -1, -1):
        space_size = 0
        space_idx = 0

        while space_idx < ubi[id_to_move] and space_size < sizes[id_to_move]:
            space_idx += space_size
            space_size = 0

            while disk[space_idx] != SPACE:
                space_idx += 1
            while (
                space_idx + space_size < len(disk)
                and disk[space_idx + space_size] == SPACE
            ):
                space_size += 1

        if space_idx >= ubi[id_to_move]:  # there is not any space
            continue

        ## Move file
        for idx in range(sizes[id_to_move]):
            disk[space_idx + idx] = id_to_move
            disk[ubi[id_to_move] + idx] = SPACE

    total = 0
    for i, id in enumerate(disk):
        if id != SPACE:
            total += i * id

    return total


if __name__ == "__main__":
    print(f"{main()}")  # 6547228115826
