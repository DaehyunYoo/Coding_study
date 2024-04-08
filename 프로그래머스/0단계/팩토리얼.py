# 팩토리얼
# https://school.programmers.co.kr/learn/courses/30/lessons/120848

def solution(n):
    answer = 0
    result = 1
    while n >= result:
        answer += 1
        result *= answer
    return answer -1