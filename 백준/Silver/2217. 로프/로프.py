n = int(input())
max_weight = []
for i in range(n):
    max_weight.append(int(input()))
max_weight.sort()

answer = []
for x in max_weight:
    answer.append(x*n)
    n -= 1

print(max(answer))