money = 1000 - int(input())
change = [500, 100, 50, 10, 5, 1]
result = 0

for i in change:
    if money == 0:
        break
    result += money // i
    money %= i
    
print(result)