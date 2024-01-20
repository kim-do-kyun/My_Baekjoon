import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
visited = [0]*(n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def DFS(v):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            DFS(i)
            
DFS(1)
for x in range(2, n+1):
    print(visited[x])