import collections
import sys

name = sys.stdin.readline().rstrip()
check_name = collections.Counter(name)  #Counter.items()로 갯수 확인
count = 0
result = ''
mid = ''
for k, v in list(check_name.items()):   # k : 알파벳, v : 알파벳 횟수
    # 알파벳의 수가 홀수라면
    if v % 2 == 1:
        count += 1
        mid = k # 중간에 들어갈 값으로 저장
        if count >= 2:  # 알파벳수가 홀수가 2개 이상이면 팰린드롬x
            print("I'm Sorry Hansoo")
            exit()

for k, v in sorted(check_name.items()): #정렬을 통해 사전순으로 for문
    result += (k*(v//2))    #정확히 절반으로 나뉜 문자열을 만들어야 하므로 현재 갯수를 2로 나눔
print(result + mid + result[::-1])