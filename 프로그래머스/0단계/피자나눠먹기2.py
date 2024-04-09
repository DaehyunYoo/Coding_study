# 피자 나눠먹기 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120815

def solution(n):
    answer = 1
    while (answer * 6) % n != 0:
        answer += 1
    return answer