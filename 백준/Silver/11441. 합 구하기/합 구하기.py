import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
num_list_sum = [0]*(N+1)

for i in range(1, N+1):
    num_list_sum[i] = num_list_sum[i-1] + num_list[i-1]

M = int(input())
for A in range(M):
    i, j = map(int, input().split())
    print(num_list_sum[j] - num_list_sum[i-1])