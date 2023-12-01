N = int(input())
row = [0] * N
result = 0
def is_threatening(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:   #열이 같거나 대각선이 같으면 False
            return False    #대각선이 같은 경우는 두 좌표에서 행 - 행 = 열 - 열 이 같으면 같은 대각선상에 있는거임
    return True

def queen(x):
    global result

    if x == N:
        result += 1
    else:
        for i in range(N):
            row[x] = i
            if is_threatening(x):
                queen(x+1)

queen(0)
print(result)
