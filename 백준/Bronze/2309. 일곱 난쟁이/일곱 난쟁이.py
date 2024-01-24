height_list = []
for _ in range(9):
    height_list.append(int(input()))
height_list.sort()
height_sum = sum(height_list)

for i in range(len(height_list)):
    for j in range(i+1, len(height_list)):
        if height_sum - height_list[i] - height_list[j] == 100:
            for k in range(len(height_list)):
                if k == i or k == j:
                    continue
                else:
                    print(height_list[k])
            exit()