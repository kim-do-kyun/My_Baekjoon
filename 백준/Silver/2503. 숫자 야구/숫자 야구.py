from itertools import permutations
num = list(range(1, 10))
num_pool = []
for i in permutations(num, 3):
    num_pool.append(i)    
n = int(input())
for _ in range(n):
    checking, st, b = map(int, input().split())
    poss = []
    for num_check in num_pool:
        strike, ball = 0, 0
        for i, check in enumerate(str(checking)):
            if int(check) == num_check[i]:
                strike += 1
            if int(check) != num_check[i] and int(check) in num_check:
                ball += 1
        if strike == st and ball == b:
            poss.append(num_check)
    num_pool = poss
print(len(poss))
