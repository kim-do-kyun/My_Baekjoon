n = int(input())
#1자리수 1개
#2자리수 1개
#3자리수 2개
#4자리수 3개
#5자리수 4개
dp = [0 for _ in range(n+1)]
dp[0], dp[1] = 1, 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n-1])