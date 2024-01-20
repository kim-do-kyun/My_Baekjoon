import sys
input = sys.stdin.readline

m = int(input())
S = set()

for _ in range(m):
    arr = list(input().split())
    order = arr[0]

    if order == 'add':
        S.add(int(arr[1]))
    elif order == 'remove':
        try:
            S.remove(int(arr[1]))
        except:
            pass
    elif order == 'check':
        if int(arr[1]) in S:
            print(1)
        else:
            print(0)
    elif order == 'toggle':
        if int(arr[1]) in S:
            S.remove(int(arr[1]))
        else:
            S.add(int(arr[1]))
    elif order == 'all':
        S = set([i for i in range(1, 21)])
    else:
        S = set()