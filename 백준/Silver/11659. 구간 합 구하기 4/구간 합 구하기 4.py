import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
prev = [0]
result = 0

for i in range(N):
    result += num_list[i]
    prev.append(result)

for num in range(M):
    i, j = map(int, input().split())
    print(prev[j] - prev[i-1])