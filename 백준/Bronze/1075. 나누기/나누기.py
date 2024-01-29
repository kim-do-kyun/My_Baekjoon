import sys
input = sys.stdin.readline
n = int(input())
f = int(input())
front = n//100
result = front*100

while result % f != 0:
    result += 1
print(str(result)[-2:])