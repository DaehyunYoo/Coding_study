# 컨트롤 제트
# https://school.programmers.co.kr/learn/courses/30/lessons/120853

def solution(s):
    answer = 0
    lst = s.split(' ')
    for i in range(len(lst)):
        if lst[i] != 'Z':
            answer += int(lst[i])
        else:
            answer -= int(lst[i-1])
    return answer