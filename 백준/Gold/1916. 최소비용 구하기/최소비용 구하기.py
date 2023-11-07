import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, [0,start])
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        for info in graph[now]:
            city, cost = info[0], info[1]
            
            cost = dist + cost
            if distance[city] > cost:
                distance[city] = cost
                heapq.heappush(q, [cost, city])

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

start, end = map(int, input().split())
dijkstra(start)

print(distance[end])