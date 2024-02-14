import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
            
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
count = 0
area = 1
result = []

def dfs(x, y):
    global area
    graph[x][y] = 1
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
            area += 1
            dfs(nx, ny)
            
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            count += 1
            dfs(i, j)
            result.append(area)
            area = 1
            
result.sort()
print(count)
print(*result)
