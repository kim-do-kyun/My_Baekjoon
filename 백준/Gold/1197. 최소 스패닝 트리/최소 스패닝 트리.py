import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def prim(start, weight):
    visit = [0]*(V+1)
    q = [[weight,start]]
    ans = 0
    cnt = 0
    while cnt < V:
        k, v = heappop(q)
        if visit[v]: continue
        visit[v] = 1
        ans += k
        cnt += 1
        for u,w in G[v]:
            heappush(q,[w,u])
    return ans

V,E = map(int, input().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, input().split())
    G[u].append([v,w])
    G[v].append([u,w])

print(prim(1,0))