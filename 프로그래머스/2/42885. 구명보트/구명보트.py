def solution(people, limit):
    #people = 사람들의 몸무게, limit = 구명보트의 무게 제한
    answer = 0
    people.sort()
    start = 0
    end = len(people) - 1
    
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1
    return answer