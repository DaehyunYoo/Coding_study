# 프로그래머스
# 공 던지기
# https://school.programmers.co.kr/learn/courses/30/lessons/120843

def solution(numbers, k):
    answer = numbers[2*(k-1) % len(numbers)]
    return answer