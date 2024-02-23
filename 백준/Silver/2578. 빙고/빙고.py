bingo_board = []
for _ in range(5):
    bingo_board.append(list(map(int, input().split())))
mc_board = []
for _ in range(5):
    mc_board += list(map(int, input().split()))

def check():
    bingo = 0
    for x in bingo_board:
        if x.count(0) == 5:
            bingo+=1
    for i in range(5):
        y = 0
        for j in range(5):
            if bingo_board[j][i] == 0:
                y += 1
        if y == 5:
            bingo+=1

    d1 = 0
    for i in range(5):
        if bingo_board[i][i] == 0:
            d1 += 1
    if d1 == 5:
        bingo += 1

    d2 = 0
    for i in range(5):
        if bingo_board[i][4-i] == 0:
            d2 += 1
    if d2 == 5:
        bingo += 1
    return bingo

count = 0

for i in range(25):
    for x in range(5):
        for y in range(5):
            if mc_board[i] == bingo_board[x][y]:
                bingo_board[x][y] = 0
                count += 1
    if count >= 12:
        result = check()

        if result >= 3:
            print(i+1)
            break
