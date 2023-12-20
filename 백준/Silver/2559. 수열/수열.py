import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))

solution = []
solution.append(sum(a[:K]))

for i in range(N - K):
    solution.append(solution[i] - a[i] + a[K+i])
    
print(max(solution))