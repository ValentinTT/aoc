from utils import read_file


def generate_expr(exp, rest):
    if rest == []:
        return [exp]

    c = generate_expr(int(str(exp) + rest[0]), rest[1:])
    s = generate_expr(exp + int(rest[0]), rest[1:])
    m = generate_expr(exp * int(rest[0]), rest[1:])
    return s + m + c


def main():
    data = read_file()
    total = 0

    for res, op in data:
        exprs = generate_expr(0, op)
        for expr in exprs:
            if expr == int(res):
                total += int(res)
                break

    return total


if __name__ == "__main__":
    print(f"{main()}")  # 162042343638683
