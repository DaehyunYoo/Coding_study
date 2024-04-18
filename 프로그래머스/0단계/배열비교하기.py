# 배열 비교하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181856

def solution(arr1, arr2):
    answer = 0
    if len(arr1) > len(arr2):
        answer = 1
    elif len(arr1) < len(arr2):
        answer = -1
    else:
        arr1_result = sum(arr1)
        arr2_result = sum(arr2)
        if arr1_result > arr2_result:
            answer = 1
        elif arr1_result < arr2_result:
            answer = -1
        else:
            answer = 0
    return answer