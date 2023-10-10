n, k = map(int, input().split())

queue = []
ans = []
num = k-1

j = 1

for i in range(n):
    queue.append(j)
    j+=1

for i in range(n):
    if len(queue) > num:
        ans.append(queue.pop(num))
        num+=k-1
    elif len(queue) <= num:
        num = num%len(queue)
        ans.append(queue.pop(num))
        num+=k-1

print("<",', '.join(str(i) for i in ans),">",sep="")
