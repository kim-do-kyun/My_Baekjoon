import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, l, total):
    global count
    if count >= total + max_pos*(4-l):
        return
    if l == 4:
        count = max(count, total)
        return
    else:
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                if l == 2:
                    visited[nx][ny] = 1
                    dfs(x, y, l+1, total+board[nx][ny])
                    visited[nx][ny] = 0
                visited[nx][ny] = 1
                dfs(nx, ny, l+1, total+board[nx][ny])
                visited[nx][ny] = 0
                
max_pos = max(map(max, board))
count = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, board[i][j])
        visited[i][j] = 0
        
print(count)