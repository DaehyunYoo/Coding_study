# 369게임
# https://school.programmers.co.kr/learn/courses/30/lessons/120891

def solution(order):
    answer = 0
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')