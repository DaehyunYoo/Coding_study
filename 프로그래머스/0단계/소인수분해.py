# 프로그래머스
# 소인수분해
# https://school.programmers.co.kr/learn/courses/30/lessons/120852

def solution(n):
    answer = []
    i = 2
    while i <= n:
        if n % i == 0:
            n /= i
            if i not in answer:
                answer.append(i)
        else:
            i += 1
    return answer