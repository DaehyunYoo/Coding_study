# 세로 읽기
# https://school.programmers.co.kr/learn/courses/30/lessons/181904

def solution(my_string, m, c):
    answer = ''
    for i in range(0, len(my_string), m):
        answer += my_string[i:i+m][c-1]
    return answer

def solution(my_string, m, c):
    return my_string[c-1::m]