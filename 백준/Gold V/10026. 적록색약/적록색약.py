import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())

graph = []
visited = [[0]*n for _ in range(n)]
sum = 0
sum2 = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    graph.append(list(input()))
    
def dfs(x, y, color):
    visited[x][y] = 1
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx <= n-1 and 0 <= ny <= n-1 and visited[nx][ny] == 0:
            if graph[nx][ny] == color:
                dfs(nx, ny, color)
                
for color in ['R', 'G', 'B']:
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] == color:
                dfs(i, j, color)
                sum += 1
                
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
            
visited = [[0]*n for _ in range(n)]

for color in ['R', 'B']:
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] == color:
                dfs(i, j, color)
                sum2 += 1
                
print(sum, sum2)