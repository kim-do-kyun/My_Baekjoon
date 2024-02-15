from collections import deque

sawtooth = [deque(list(map(int, input()))) for _ in range(4)]
k = int(input())

# 오른쪽 톱니바퀴
def right(idx, d):
    # 마지막 톱니바퀴는 확인x
    if idx > 3:
        return
    # 같은 극이 아니면 회전
    if sawtooth[idx-1][2] != sawtooth[idx][6]:
        right(idx + 1, -d)
        sawtooth[idx].rotate(d)

# 왼쪽 톱니바퀴
def left(idx, d):
    # 첫번째 톱니바퀴 확인x
    if idx < 0:
        return
    if sawtooth[idx][2] != sawtooth[idx+1][6]:
        left(idx-1, -d)
        sawtooth[idx].rotate(d)

for _ in range(k):
    idx, d = map(int, input().split())
    idx -= 1
    # 톱니번호가 회전하는 방향의 반대방향으로 회전하므로 -d
    left(idx-1, -d)
    right(idx+1, -d)

    # 회전할 톱니 번호의 톱니 회전
    sawtooth[idx].rotate(d)

score = 0
for i in range(4):
    if sawtooth[i][0] == 1:
        score += 2**i

print(score)