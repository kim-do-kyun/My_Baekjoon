n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = []

def dfs():
    if len(result) == m:
        print(*result)
        return
    for i in range(n):
        if nums[i] not in result:
            result.append(nums[i])
            dfs()
            result.pop()
            
dfs()