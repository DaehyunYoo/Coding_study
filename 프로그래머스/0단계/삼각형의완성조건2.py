# 삼각형의 완성 조건2
# https://school.programmers.co.kr/learn/courses/30/lessons/120868

def solution(sides):
    answer = 0
    for i in range(1, sum(sides)):
        if i >= max(sides) and i < sum(sides):
            answer += 1

        if max(sides) > i and (i+min(sides)) > max(sides):
            answer += 1

    return answer