# 배열에서 문자열 대소문자 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181875

def solution(strArr):
    answer = []
    for i in range(0, len(strArr)):
        if i % 2 == 0:
            strArr[i] = strArr[i].lower()
        elif i % 2 != 0:
            strArr[i] = strArr[i].upper()
    return strArr