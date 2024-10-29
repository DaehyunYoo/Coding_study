# 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for b in range(1, total + 1):
        if (total / b) % 1 == 0:
            a = total / b
            if a >= b:
                if a*2 + b*2 == brown + 4:
                    return [a, b]