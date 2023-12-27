def solution(array, commands):
    answer = []
    for i in commands:
        check = array[i[0]-1 : i[1]]
        check.sort()
        answer.append(check[i[2]-1])
        
    return answer