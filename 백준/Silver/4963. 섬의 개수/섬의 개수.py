import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def DFS(x, y):
    visited[x][y] = 1
    if graph[x][y] == 1:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    DFS(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    visited = [[0]*w for _ in range(h)]
    graph = []
    result = 0
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    for x in range(h):
        for y in range(w):
            if not visited[x][y] and graph[x][y] == 1:
                DFS(x, y)
                result += 1
    print(result)