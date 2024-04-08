# k의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120887

def solution(i, j, k):
    answer = 0

    for x in range(i, j+1):
        for y in str(x):
            if str(k) in y:
                answer += 1
    return answer