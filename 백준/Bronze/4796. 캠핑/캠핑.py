import sys
input = sys.stdin.readline
case_count = 1
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    # P일 중 L일만 사용할 수 있음
    using_day = ((V//P)*L + min((V%P), L))
    print(f'Case {case_count}: {using_day}')
    case_count += 1