import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    rank = list(list(map(int, input().split())) for _ in range(N))
    rank_sort = sorted(rank)
    top = 0
    result = 1
        
    for i in range(1, len(rank_sort)):
        if rank_sort[i][1] < rank_sort[top][1]:
            top = i
            result += 1
    print(result)