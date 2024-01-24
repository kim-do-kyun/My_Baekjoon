n = int(input())
day_list = []
for _ in range(n):
    day_list.append(list(map(int, input().split())))
    
dp = [0 for i in range(n+1)]

for i in range(n):
    for j in range(i+day_list[i][0], n+1):
        if dp[j] < dp[i] + day_list[i][1]:
            dp[j] = dp[i] + day_list[i][1]
            
print(dp[-1])