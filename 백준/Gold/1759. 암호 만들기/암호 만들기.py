import sys
from itertools import combinations
input = sys.stdin.readline
l, c = map(int, input().split())
alpha = input().split()

alpha_combi = combinations(sorted(alpha), l)

result = []

for i in alpha_combi:
    consonant_count = 0
    vowel_count = 0
    
    for alpha in i:
        if alpha in "aeiou":
            consonant_count += 1
        else:
            vowel_count += 1
    if consonant_count >= 1 and vowel_count >= 2:
        print("".join(i))