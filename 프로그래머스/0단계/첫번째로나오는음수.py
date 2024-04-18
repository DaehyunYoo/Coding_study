# 첫 번째로 나오는 음수
# https://school.programmers.co.kr/learn/courses/30/lessons/181896

def solution(num_list):
    answer = 0
    for idx, val in enumerate(num_list):
        if val < 0: # while val < 0: 도 상관 없음
            return idx
    return -1