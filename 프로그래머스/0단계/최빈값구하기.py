# 최빈값 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120812

def solution(array):        
    while len(array) != 0:
        for idx, val in enumerate(set(array)):
            array.remove(val)
        if idx == 0: 
            return val
    return -1