n,k = map(int, input().split())

value = []
count = 0
for i in range(n):
    value.append(int(input()))

value.sort(reverse=True)

for i in range(n):
    if k==0:
        break
    if k//value[i] != 0:
        count+=k // value[i]
        k = k % value[i]
print(count)