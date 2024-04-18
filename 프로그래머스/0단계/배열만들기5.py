# 배열 만들기 5
# https://school.programmers.co.kr/learn/courses/30/lessons/181912

def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        x = i[s:s+l]
        if int(x) > k:
            answer.append(int(x))
    return answer