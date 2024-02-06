n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = []
visited = [False]*n

def dfs():
    if len(result) == m:
        print(*result)
        return
    temp = 0
    for i in range(n):
        if not visited[i] and temp != nums[i]:
            visited[i] = True
            result.append(nums[i])
            temp = nums[i]
            dfs()
            visited[i] = False
            result.pop()

dfs()