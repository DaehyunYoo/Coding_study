# n의 배수 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/120905

def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer


def solution(n, numlist):
    answer = [i for i in numlist if i%n==0]
    return answer