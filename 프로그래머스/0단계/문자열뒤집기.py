# 문자열 뒤집기
# https://school.programmers.co.kr/learn/courses/30/lessons/181905

def solution(my_string, s, e):
    answer = ''
    x = my_string[s:e+1][::-1]
    answer = my_string[:s] + x + my_string[e+1:]
    return answer

def solution(my_string, s, e):
    substr = reversed(list(my_string[s:e+1]))
    return my_string[:s] + ''.join(substr) + my_string[e+1:]