N, M = map(int, input().split())

array = []

def dfs(start):
    if len(array) == M:
        for i in array:
            print(i, end=' ')
        print()
        return
    for i in range(start, N+1):
        array.append(i)
        dfs(i)
        array.pop()
dfs(1)