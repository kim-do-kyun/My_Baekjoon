import sys, heapq
input = sys.stdin.readline
n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))
    
total_cost = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    sum_value = a + b
    
    total_cost += sum_value
    heapq.heappush(cards, sum_value)
    
print(total_cost)