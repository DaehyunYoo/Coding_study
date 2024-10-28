# 2의 영역
# https://school.programmers.co.kr/learn/courses/30/lessons/181894

def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]

def solution(arr):
    answer = []
    lst=[]
    if 2 not in arr:
        return [-1]
    else:
        for i in range(0, len(arr)):
            if arr[i]==2:
                lst.append(i)
    return arr[lst[0]:lst[-1]+1]