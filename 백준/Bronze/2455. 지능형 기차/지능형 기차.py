
max_count = 0
current_count = 0
for _ in range(4):
    a, b = map(int, input().split())
    current_count += (b-a)
    if max_count < current_count:
        max_count = current_count

print(max_count)