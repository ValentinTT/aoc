from utils import read_file

def main():
    data = read_file()
    n = len(data)
    m = len(data[0])

    def has_xmas(i, j):
        if i < 1 or i >= n - 1 or j < 1 or j >= m - 1:
            return False
        if data[i][j] != "A":
            return False
        top_l = data[i-1][j-1] + data[i+1][j+1]
        top_r = data[i-1][j+1] + data[i+1][j-1]
        corners = ["MS", "SM"]
        return top_l in corners and top_r in corners

    res = 0

    for i in range(n):
        for j in range(m):
            res += has_xmas(i, j)

    return res

if __name__ == "__main__":
    print(f"xmas: {main()}")