import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
broken_btns = list(map(int, input().split()))

min_count = abs(100-n)

for nums in range(1000001):
    nums = str(nums)
    for j in range(len(nums)):
        if int(nums[j]) in broken_btns:
            break
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums)-n)+len(nums))
            
print(min_count)