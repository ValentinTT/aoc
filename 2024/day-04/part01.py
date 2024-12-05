from utils import read_file

def main():
    data = read_file()
    n = len(data)
    m = len(data[0])

    directions = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                directions.append((dx, dy))
    

    def has_xmas(i, j, d):
        dx, dy = d
        for k, x in enumerate("XMAS"):
            i2 = i + dx*k 
            j2 = j + dy*k
            if i2 < 0 or i2 >= n or j2 < 0 or j2 >= m:
                return False
            if data[i2][j2] != x:
                return False
        return True

    res = 0

    for i in range(n):
        for j in range(m):
            for d in directions:
                res = res + 1 if has_xmas(i, j, d) else res

    return res

if __name__ == "__main__":
    print(f"xmas: {main()}") # 2571