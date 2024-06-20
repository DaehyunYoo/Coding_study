# 다음 큰 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = n
    while True:
        answer += 1
        if str(bin(n))[2:].count('1') == str(bin(answer))[2:].count('1'):
            break
    return answer