import sys
input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0]*m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
visited[r][c] = 1

while True:
    flag = 0
    for _ in range(4):
        nx = r+dx[(d+3)%4]
        ny = c+dy[(d+3)%4]

        # 한번 돌았으면 그 방향을 작업
        d = (d+3)%4
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                count += 1
                r = nx
                c = ny
                # 청소 한 방향이라도 했으면 다음으로 넘어감
                flag = 1
                break

    if flag == 0:   # 4방향 모두 청소가 되었을때
        if graph[r-dx[d]][c-dy[d]] == 1:    # 후진했는데 벽일때
            print(count)
            break
        else:
            r, c = r-dx[d], c-dy[d]
