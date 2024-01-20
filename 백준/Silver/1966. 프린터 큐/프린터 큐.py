T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    index = [i for i in range(n)]
    index[m] = 'target'
    count = 0
    
    while priority:
        if priority[0] == max(priority):
            count += 1
            if index[0] == 'target':
                print(count)
                break
            priority.pop(0)
            index.pop(0)
        else:
            priority.append(priority.pop(0))
            index.append(index.pop(0))