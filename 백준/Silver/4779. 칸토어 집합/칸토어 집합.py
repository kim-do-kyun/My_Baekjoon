import sys
input = sys.stdin.readline

def cantor(start, n):
    if n==1:
        return
    for i in range(start + n//3, start+(n//3)*2):
        result[i] = ' '
    cantor(start, n//3)
    cantor(start + n//3*2, n//3)

while True:
    try :
        n = int(input())
        result = ['-']*(3**n)
        cantor(0,3**n)
        print(''.join(result))
    except:
        break
