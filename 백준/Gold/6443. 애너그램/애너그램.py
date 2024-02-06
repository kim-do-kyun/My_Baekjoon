import sys
n = int(sys.stdin.readline())

def back(count):
    if count == len(word):
        print("".join(answer))
        return
    for i in visited:
        if visited[i]:
            visited[i] -= 1
            answer.append(i)
            back(count+1)
            visited[i] += 1
            answer.pop()
            
for _ in range(n):
    word = sorted(list(map(str, input().strip())))
    visited = {}
    answer = []
    
    for i in word:
        if i in visited:
            visited[i] += 1
        else:
            visited[i] = 1
            
    back(0)
            