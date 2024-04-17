# 원하는 문자열 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/181878

def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()

    if pat in myString:
        return 1
    else:
        return 0
    
def solution(myString, pat):
    return int(pat.lower() in myString.lower())