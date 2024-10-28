# 중복된 문자 제거
# https://school.programmers.co.kr/learn/courses/30/lessons/120888

def solution(my_string):
    answer = ''
    for i in list(my_string):
        if i not in answer:
            answer += i
    return answer