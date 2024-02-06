n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = []

def dfs(start):
    if len(result) == m:
        print(*result)
        return
    temp = 0
    for i in range(start, n):
        if temp != nums[i]:
            result.append(nums[i])
            temp = nums[i]
            dfs(i+1)
            result.pop()

dfs(0)
