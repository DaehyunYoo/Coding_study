# 특정한 문자를 대문자로 바꾸기
# https://school.programmers.co.kr/learn/courses/30/lessons/181873

def solution(my_string, alp):
    answer = ''
    for idx, val in enumerate(my_string):
        if val == alp:
            answer += val.upper()
        else:
            answer += val
    return answer

def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())