import sys
input = sys.stdin.readline
N, L = map(int, input().split())
water_leak = list(map(int, input().split()))

water_leak.sort()

start = water_leak[0]
count = 1

for location in water_leak[1:]:
    if location in range(start, start+L):
        continue
    else:
        start = location
        count += 1
        
print(count)