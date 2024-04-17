# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/181872

def solution(myString, pat):
    end = myString.rfind(pat)

    return myString[:end + len(pat)]