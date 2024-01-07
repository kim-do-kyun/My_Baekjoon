import sys
input = sys.stdin.readline

N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
B = map(int, input().split())

def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == A[m]:
        return 1
    elif l < A[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

for l in B:
    start = 0
    end = len(A)-1
    print(binary(l, N, start, end))
