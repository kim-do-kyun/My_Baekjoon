import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

dp = [0 for _ in range(M+1)]
memo = []

for _ in range(N):
    w,c,k = map(int, input().split(' '))
    i = 1
    while k > 0:
        m = min(i, k)
        memo.append((w*m, c*m))
        k -= i
        i *= 2
        
for w, c in memo:
    for i in range(M, w-1, -1):
        dp[i] = max(dp[i], dp[i-w] + c)
print(dp[M])