def solution(a, b):
    answer = 0
    result1 = str(a)+str(b)
    result1 = int(result1)
    
    result2 = 2*a*b
    if result1 == result2:
        answer = result1
    else:
        answer = max(result1, result2)
    return answer