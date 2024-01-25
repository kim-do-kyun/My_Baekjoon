n = int(input())
number = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_value = - int(1e9)
min_value = int(1e9)

def dfs(add, sub, mul, div, sum, idx):
    global max_value, min_value
    if idx == n:
        max_value = max(max_value, sum)
        min_value = min(min_value, sum)
        return
    if add:
        dfs(add-1, sub, mul, div, sum+number[idx], idx+1)
    if sub:
        dfs(add, sub-1, mul, div, sum-number[idx], idx+1)
    if mul:
        dfs(add, sub, mul-1, div, sum*number[idx], idx+1)
    if div:
        dfs(add, sub, mul, div-1, int(sum/number[idx]), idx+1)

dfs(add, sub, mul, div, number[0], 1)
print(max_value)
print(min_value)