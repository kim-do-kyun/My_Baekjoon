N = int(input())
first_word = list(input())

for i in range(N-1):
    other_word = list(input())
    for j in range(len(first_word)):
        if first_word[j] != other_word[j]:
            first_word[j] = '?'
            
print(''.join(first_word))