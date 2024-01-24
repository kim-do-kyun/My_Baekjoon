n, m = map(int, input().split())
boards = []
count = []
for i in range(n):
    boards.append(input())
    
for i in range(n-7):
    for j in range(m-7):
        white = 0
        black = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if boards[x][y] == 'B':
                        white += 1
                    else:
                        black += 1
                else:
                    if boards[x][y] == 'B':
                        black += 1
                    else:
                        white += 1
        count.append(white)
        count.append(black)
print(min(count))