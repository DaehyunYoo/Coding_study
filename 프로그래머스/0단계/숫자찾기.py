# 숫자 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/120904

def solution(num, k):
    k = str(k)
    lst = str(num)

    if k in lst:
        return lst.find(k) + 1
    else:
        return -1
    
def solution(num, k):
    for i, n in enumerate(str(num)):
        if str(k) == n:
            return i + 1
    return -1