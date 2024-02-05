import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    num_list = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * n for _ in range(2)]

    #스티커 길이가 1인 경우
    dp[0][0] = num_list[0][0]
    dp[1][0] = num_list[1][0]
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    #스티커 길이가 2인 경우
    dp[0][1] = num_list[1][0] + num_list[0][1]
    dp[1][1] = num_list[0][0] + num_list[1][1]
    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    #스티커 길이가 3인경우
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + num_list[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + num_list[1][i]

    print(max(dp[0][-1], dp[1][-1]))