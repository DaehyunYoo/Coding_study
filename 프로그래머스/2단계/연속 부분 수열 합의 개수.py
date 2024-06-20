# 연속 부분 수열 합의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/131701


def solution(elements):
    answer = set()
    new_elements = elements * 2
    for i in range(len(elements)):
        for j in range(len(elements)):
            sum_result = sum(new_elements[j:j+i+1])
            answer.add(sum_result)
    
    
    return len(answer)