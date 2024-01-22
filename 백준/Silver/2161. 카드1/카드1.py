n = int(input())
cards = [i for i in range(1, n+1)]
answer = []

while len(cards) != 0:
    answer.append(cards.pop(0))
    if len(cards) != 0:
        cards.append(cards.pop(0))
       
for j in answer:
    print(j, end=" ")