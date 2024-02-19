H, W = map(int, input().split())
bound = list(map(int, input().split()))

area = 0
for i in range(1, W-1):
    left_max = max(bound[:i])
    right_max = max(bound[i+1:])
    
    compare = min(left_max, right_max)
    
    if bound[i] < compare:
        area += compare - bound[i]
        
print(area)