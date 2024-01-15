import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    dp = [0] * N
    dp[0] = num_list[0]
    for i in range(1, N):
        dp[i] = max(dp[i-1] + num_list[i], num_list[i])
    print(max(dp))