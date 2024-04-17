# 배열 만들기 6
# https://school.programmers.co.kr/learn/courses/30/lessons/181859

def solution(arr):
    stk = []

    for i in range(len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
        else:
            if stk[-1] == arr[i]:
                stk.pop()
                i += 1
            elif stk[-1] != arr[i]:
                stk.append(arr[i])
                i += 1
    if len(stk) == 0:
        return [-1]

    return stk

def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk and stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])

    return stk or [-1]