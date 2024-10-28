# 간단한 식 계산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181865

def solution(binomial):
    answer = 0
    a, op, b = binomial.split(' ')
    if op == '+':
        answer = int(a) + int(b)
    elif op == '-':
        answer = int(a) - int(b)
    else:
        answer = int(a) * int(b)
    return answer

def solution(binomial):
    return eval(binomial)