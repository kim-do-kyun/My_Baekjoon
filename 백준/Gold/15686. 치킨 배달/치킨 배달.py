import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
city_info = list(list(map(int, input().split())) for _ in range(n))
result = float('inf')
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if city_info[i][j] == 1:
            house.append([i, j])
        elif city_info[i][j] == 2:
            chicken.append([i, j])
            
for c in combinations(chicken, m):
    temp = 0
    for h in house:
        chicken_length = float('inf')
        for j in range(m):
            chicken_length = min(chicken_length, abs(h[0]-c[j][0]) + abs(h[1]-c[j][1]))
        temp += chicken_length
    result = min(result, temp)
print(result)   