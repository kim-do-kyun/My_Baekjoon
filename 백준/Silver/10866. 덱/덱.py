import sys

n = int(sys.stdin.readline())
deck = []

for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == "push_front":
        deck.insert(0,order[1])
    elif order[0] == "push_back":
        deck.append(order[1])
    elif order[0] == "pop_front":
        if len(deck)==0:
            print("-1")
        else:
            print(deck.pop(0))
    elif order[0] == "pop_back":
        if len(deck)==0:
            print("-1")
        else:
            print(deck.pop(len(deck)-1))
    elif order[0] == "size":
        print(len(deck))
    elif order[0] == "empty":
        if len(deck) == 0:
            print("1")
        else:
            print("0")
    elif order[0] == "front":
        if len(deck) == 0:
            print("-1")
        else:
            print(deck[0])
    else:
        if len(deck) == 0:
            print("-1")
        else:
            print(deck[len(deck)-1])