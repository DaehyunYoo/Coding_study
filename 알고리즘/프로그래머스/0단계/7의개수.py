# 7의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120912

def solution(array):
    answer = 0
    for i in array:
        answer += str(i).count('7')
    return answer