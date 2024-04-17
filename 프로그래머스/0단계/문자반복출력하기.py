# 문자 반복 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120825

def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i * n
    return answer

def solution(my_string, n):
    answer = []
    for i in my_string:
        answer.append(i * n)

    return ''.join(answer)