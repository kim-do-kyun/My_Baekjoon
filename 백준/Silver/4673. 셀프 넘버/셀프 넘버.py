def makeNum(num):
    num = num + sum(map(int, str(num)))
    return num

nonSelfNum = set()

for i in range(1, 10001):
    nonSelfNum.add(makeNum(i))
    
for j in range(1, 10001):
    if j not in nonSelfNum:
        print(j)