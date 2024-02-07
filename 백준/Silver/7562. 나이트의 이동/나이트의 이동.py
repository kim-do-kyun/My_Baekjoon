import sys
input = sys.stdin.readline
t = int(input())
x = [1, -1, 1, -1, 2, -2, 2, -2]
y = [2, 2, -2, -2, 1, 1, -1, -1]

def bfs(c_x, c_y):
    queue = []
    queue.append((c_x, c_y))
    c[c_x][c_y] += 1
    while queue:
        c_x, c_y = queue.pop(0)
        if c_x == e_x and c_y == e_y:
            return c[c_x][c_y]
        for dx, dy in zip(x, y):
            nx = c_x + dx
            ny = c_y + dy
            if 0 <= nx < l and 0<= ny < l and c[nx][ny] == -1:
                queue.append((nx, ny))
                c[nx][ny] = c[c_x][c_y] + 1
    
    
for _ in range(t):
    l = int(input())
    c = [[-1]*l for _ in range(l)]
    s_x, s_y = map(int, input().split())
    e_x, e_y = map(int, input().split())
    print(bfs(s_x, s_y))