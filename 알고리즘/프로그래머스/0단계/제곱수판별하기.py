# 제곱수 판별하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120909

def solution(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return 1
    else:
        return 2
    