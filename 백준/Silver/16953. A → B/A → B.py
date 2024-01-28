import sys
input = sys.stdin.readline
a, b = map(int, input().split())
end = 1
while b!=a:
    end += 1
    temp = b
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    
    if temp == b:
        print(-1)
        break
else:
    print(end)