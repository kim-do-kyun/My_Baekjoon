import sys
input = sys.stdin.readline

n, k = map(int, input().split())
memo = {}
for i in range(n):
    w, v = map(int, input().split())
    memo[i] = (w,v)
    
list = [[0]*(k+1) for _ in range(n)]

firstline = memo[0]
firstw, firstv = firstline

for i in range(1, k+1):
    if firstw <= i:
        list[0][i] = firstv
    else:
        list[0][i] = 0
for r in range(1, n):
    weight, value = memo[r]
    for c in range(1, k+1):
        if weight <= c:
            list[r][c] = max(list[r-1][c], value + list[r-1][c-weight])
        else:
            list[r][c] = list[r-1][c]
print(list[-1][-1])