from collections import deque
MAX = 100000
dist = [0]*(MAX+1)

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for j in (x-1,x+1,x*2):
            if 0<= j <= MAX and not dist[j]:
                dist[j] = dist[x]+1
                q.append(j)
                
n, k = map(int, input().split())
bfs()