# 문자열안에 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/120908

def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2