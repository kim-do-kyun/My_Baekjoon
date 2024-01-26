n = int(input())
road_length = list(map(int, input().split()))
oil_amount = list(map(int, input().split()))

min_value = oil_amount[0]
total = 0

for i in range(n-1):
    if min_value > oil_amount[i]:
        min_value = oil_amount[i]
    total += (min_value * road_length[i])
    
print(total)