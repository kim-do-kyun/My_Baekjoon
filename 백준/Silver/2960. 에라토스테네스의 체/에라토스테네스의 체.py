n, k = map(int, input().split())
count = 0
nums = [True]*(n+1)
for i in range(2, len(nums)+1):
    for j in range(i, n+1, i):
        if nums[j] != False:
            nums[j] = False
            count += 1
            if count == k:
                print(j)
                break