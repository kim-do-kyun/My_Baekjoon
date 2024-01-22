import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
bound = [list(map(int, input().split())) for _ in range(n)]
answer = sys.maxsize
idx = 0

for floor in range(257):
    max_block, min_block = 0, 0
    for i in range(n):
        for j in range(m):
            if bound[i][j] > floor:
                max_block += bound[i][j] - floor
            else:
                min_block += floor - bound[i][j]
                
    if max_block + b >= min_block:
        if min_block + (max_block*2) <= answer:
            answer = min_block + (max_block*2)
            idx = floor
            
print(answer, idx)