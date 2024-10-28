# 문자열 잘라서 정렬하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181866

def solution(myString):
    answer = []
    print(myString.split('x'))
    answer = sorted(filter(None, myString.split('x')))
    return answer

def solution(myString):
    return sorted([i for i in myString.split("x") if len(i)!=0])