def solution(n, lost, reserve): 
    # n = 전체 학생 수, lost = 도난당한 학생들의 번호가 담긴 배열, reserve = 여벌의 체육복을 가져온 학생들의 번호
    #lost에 있는 항목들 중 +-1의 범위에서 reserve에 있는 항목은 다 없애주고 전체 학생 수에서 lost의 길이를 빼주면 되는 문제
    _lost = set(lost) - set(reserve)
    _reserve = set(reserve) - set(lost)
    
    for idx in _reserve:
        if idx - 1 in _lost:
            _lost.remove(idx-1)
        elif idx + 1 in _lost:
            _lost.remove(idx+1)
    return n - len(_lost)