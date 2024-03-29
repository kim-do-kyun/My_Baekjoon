from collections import deque
T = int(input())
for i in range(T):
    p = input()
    n = int(input())
    num_list = input()[1:-1].split(',')
    
    queue = deque(num_list)
    
    flag = 0
    
    if n == 0:
        queue = []
        
    for j in p:
        if j == 'R':
            flag += 1
        elif j == 'D':
            if len(queue) == 0:
                print("error")
                break
            else:
                if flag % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    else:
        if flag % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")