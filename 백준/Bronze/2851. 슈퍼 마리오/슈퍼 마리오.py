import sys
input = sys.stdin.readline
arr = []
sum = 0
for i in range(10):
    arr.append(int(input()))
for j in arr:
    sum += j
    if sum >= 100:
        if sum - 100 > 100 - (sum - j):
            sum -= j
        break
print(sum)