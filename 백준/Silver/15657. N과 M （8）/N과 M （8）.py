n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = []

def dfs(start):
    if len(result) == m:
        print(*result)
        return
    for i in range(start, n):
        result.append(nums[i])
        dfs(i)
        result.pop()
        
dfs(0)