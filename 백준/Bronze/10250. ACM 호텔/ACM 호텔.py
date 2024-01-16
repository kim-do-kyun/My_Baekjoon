T = int(input())
for i in range(T):
    h, w, n = map(int, input().split())
    floor = n%h
    rooms = (n//h) + 1
    if floor == 0:
        floor = h
        rooms -= 1
    print(floor*100 + rooms)