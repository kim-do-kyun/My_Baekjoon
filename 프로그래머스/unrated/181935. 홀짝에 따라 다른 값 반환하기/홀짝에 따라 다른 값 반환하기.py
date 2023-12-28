def solution(n):
    sum, sum_2 = 0, 0
    if n % 2 == 1:
        for i in range(n+1):
            if i % 2 == 1:
                sum += i
        return sum
    else:
        for i in range(n+1):
            if i % 2 == 0:
                sum_2 += i*i
        return sum_2
        