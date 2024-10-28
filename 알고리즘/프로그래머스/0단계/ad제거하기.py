# ad 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181870

def solution(strArr):
    answer = []
    for i in strArr:
        if "ad" not in i:
            answer.append(i)
    return answer