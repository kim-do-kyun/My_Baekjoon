import sys
s = sys.stdin.readline().strip()+' '
stack = []
result = ''
check = 0
for i in s:

    if i == "<":
        check=1
        for _ in range(len(stack)):
            result += stack.pop()
    stack.append(i)
    if i==">":
        check = 0
        for _ in range(len(stack)):
            result += stack.pop(0)

    if i==" " and check==0:
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += " "

print(result)
