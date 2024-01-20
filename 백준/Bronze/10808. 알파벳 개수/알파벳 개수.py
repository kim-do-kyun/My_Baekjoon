s = input()
arr = [0]*26
for str in s:
    arr[ord(str)-97] += 1
print(*arr)