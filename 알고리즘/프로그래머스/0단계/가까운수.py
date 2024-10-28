# 가까운 수
# https://school.programmers.co.kr/learn/courses/30/lessons/120890

def solution(array, n):
    array.sort()
    answer = array[0]
    x = abs(n - answer)

    for i in array:
        if x > abs(n - i):
            x = abs(n - i)
            answer = i
    return answer