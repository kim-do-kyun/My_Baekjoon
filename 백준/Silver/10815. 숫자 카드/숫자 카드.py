import sys
n = int(sys.stdin.readline())
num_card = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
check_card = list(map(int, sys.stdin.readline().split()))

for check in check_card:
    low, high = 0, n-1
    exit = False
    while low <= high:
        mid = (low+high)//2
        if num_card[mid] > check:
            high = mid -1
        elif num_card[mid] < check:
            low = mid + 1
        else:
            exit = True
            break
    print(1 if exit else 0, end=' ')