# JadenCase 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    
    words = s.split(' ')
    
    for i in words:
        for j in range(len(i)):
            if j == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        if i == words[-1]:
            pass
        else:
            answer += ' '
    return answer