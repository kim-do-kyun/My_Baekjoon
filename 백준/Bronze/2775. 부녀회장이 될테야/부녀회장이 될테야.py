import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    peoples = [i for i in range(1, n+1)]
    
    for x in range(k):
        for y in range(1, n):
            peoples[y] += peoples[y-1]
    print(peoples[-1])