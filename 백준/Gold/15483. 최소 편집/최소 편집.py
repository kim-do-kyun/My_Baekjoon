import sys
input = sys.stdin.readline

S = input()
T = input()

m = len(S)
n = len(T)

#m이 n보다 더큰듯
if m < n:
    n, m = m, n
    S, T = T, S

E = [[_ for _ in range(n+1)] for _ in range(m+1)]

for i in range(m+1):
    E[i][0] = i
for j in range(n+1):
    E[0][j] = j

for j in range(1, n+1):
    for i in range(1, m+1):
        if S[i - 1] == T[j - 1]:
            alpha = 0
        else:
            alpha = 1
        E[i][j] = min(E[i-1][j] + 1, E[i][j-1] + 1, E[i-1][j-1] + alpha)

print(E[m][n])