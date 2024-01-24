n = int(input())
people_list = []
for i in range(n):
    people_list.append(list(map(int, input().split())))
    
for i in people_list:
    rank = 1
    for j in people_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")