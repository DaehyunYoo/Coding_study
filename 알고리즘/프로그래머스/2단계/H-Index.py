# H-Index
# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    h_index = 0
    
    for i in citations:
        if i > h_index:
            h_index += 1

    return h_index