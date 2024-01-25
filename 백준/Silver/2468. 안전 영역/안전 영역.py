import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
N = int(input())
bound = [list(map(int, input().split())) for _ in range(N)]
maxsafezone = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, rain):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and bound[nx][ny] > rain:
            dfs(nx, ny, rain)
    return True

for rain in range(1, 101):
    visited = [[False for _ in range(N)] for _ in range(N)]
    safezone = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and bound[i][j] > rain:
                safezone += 1
                dfs(i, j, rain)
    maxsafezone = max(maxsafezone, safezone)
print(maxsafezone)