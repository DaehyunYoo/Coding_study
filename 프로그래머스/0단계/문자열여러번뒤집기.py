# 문자열 여러번 뒤집기
# https://school.programmers.co.kr/learn/courses/30/lessons/181913

def solution(my_string, queries):
    answer = ''
    for i, j in queries:
        my_string = my_string[:i] + my_string[i:j+1][::-1] + my_string[j+1:]
    answer = my_string
    return answer

def solution(my_string, queries):
    answer=list(my_string)
    for s,e in queries:
        answer[s:e+1]=answer[s:e+1][::-1]
    return ''.join(answer)