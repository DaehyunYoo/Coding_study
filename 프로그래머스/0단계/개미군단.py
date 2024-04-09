# 개미 군단
# https://school.programmers.co.kr/learn/courses/30/lessons/120837

def solution(hp):
    x = (hp // 5)
    y = (hp - 5 * x) // 3
    z = (hp - 5 * x) % 3
    return x + y + z