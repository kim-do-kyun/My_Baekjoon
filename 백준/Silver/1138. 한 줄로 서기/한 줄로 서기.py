n = int(input())
n_list = list(map(int, input().split()))
cm = list(range(1, n+1))
result = []

j = -1
for i in range(n):
    result.insert(n_list[j], cm[j])
    j -= 1
    
for i in result:
    print(i, end=' ')