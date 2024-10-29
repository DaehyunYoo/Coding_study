# 문자열 묶기
# https://school.programmers.co.kr/learn/courses/30/lessons/181855

def solution(strArr):
    answer = 0
    length = [] 
    for i in strArr:
        length.append(len(i))

    result = [0] * max(length) # 길이 개수를 담을 result 리스트

    for idx, val in enumerate(length):
        result[val-1] += 1

    answer = max(result)


    return answer