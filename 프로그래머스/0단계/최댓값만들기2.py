# 최댓값 만들기 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120862

def solution(numbers):
    answer = 0
    numbers.sort() 

    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])