def solution(n):
    answer = 0
    fibo_num = fibo(n)
    if n >= 2:
        return fibo_num % 1234567
    else:
        return n

def fibo(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

        
    