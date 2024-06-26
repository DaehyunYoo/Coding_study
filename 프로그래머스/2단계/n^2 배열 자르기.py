# n^2 배열 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        a = i // n 
        b = i % n
        if a < b:
            a, b = b, a
        answer.append(a+1)
    return answer