import sys
from itertools import permutations
input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split()))

per = permutations(num_list)
result = 0

for i in per:
    s = 0
    for j in range(len(i)-1):
        s += abs(i[j] - i[j+1])
    if s > result:
        result = s
print(result)