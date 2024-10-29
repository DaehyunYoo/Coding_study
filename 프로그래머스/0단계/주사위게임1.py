# 주사위 게임 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181839

def solution(a, b):

    if a % 2 != 0 and b % 2 != 0:
        return a**2 + b**2
    elif a % 2 == 0 and b % 2 == 0:
        return abs(a - b)
    else:
        return 2 * (a + b)