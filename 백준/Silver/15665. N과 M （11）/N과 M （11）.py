n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = []

def dfs():
    if len(result) == m:
        print(*result)
        return
    temp = 0
    for i in range(n):
        if temp != nums[i]:
            result.append(nums[i])
            temp = nums[i]
            dfs()
            result.pop()

dfs()