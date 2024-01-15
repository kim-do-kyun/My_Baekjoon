N, K = map(int, input().split())
temp_list = list(map(int, input().split()))

total_temp = []

for i in range(N - K + 1):
    total = 0
    for j in range(i, i + K):
        total += temp_list[j]
    total_temp.append(total)
print(max(total_temp))