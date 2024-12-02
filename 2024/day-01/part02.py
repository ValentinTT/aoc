from utils import read_file
        
def main():
    l, r = read_file()
    counter_r = {}
    similarity_score = 0

    for n in r:
        counter_r[n] = counter_r.get(n, 0) + 1
    
    for n in l:
        similarity_score += (n * counter_r.get(n, 0))

    return similarity_score

if __name__ == "__main__":
    print(f"Similarity score {main()}") # 23384288