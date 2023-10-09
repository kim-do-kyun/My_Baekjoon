import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    index = sys.stdin.readline().split()
    if len(index)==2 and index[0]=="push":
        stack.append(index[1])
    elif len(index)==1 and index[0]=="top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    elif len(index)==1 and index[0]=="size":
        print(len(stack))
    elif len(index)==1 and index[0]=="pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif len(index)==1 and index[0]=="empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)