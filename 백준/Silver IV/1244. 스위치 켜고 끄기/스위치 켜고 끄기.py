def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

n = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    sex, num = map(int, input().split())
    #남자일때
    if sex == 1:
        for i in range(num, n+1, num):
            change(i)
    #여자
    else:
        change(num)
        for k in range(n//2):
            if num + k > n or num - k < 1: break
            if switch[num+k] == switch[num-k]:
                change(num+k)
                change(num-k)
            else:
                break

for i in range(1, n+1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()