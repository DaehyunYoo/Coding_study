# 멀리 뛰기
# https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    answer = [i for i in range(n+1)]
    for i in range(3, n+1):
        answer[i] = answer[i-1] + answer[i-2]
    
    return answer[n] % 1234567