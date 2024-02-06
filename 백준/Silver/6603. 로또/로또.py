from itertools import combinations
while True:
    n = input().split()
    if n[0] == "0":
        break
        
    s = n[1:]
    for c in combinations(s, 6):
        print(" ".join(c))
    print()