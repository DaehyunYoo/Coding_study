# 가가운 1 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/181898

def solution(arr, idx):
    answer = -1
    result = []
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            result.append(i)
            answer = result[0]
            break
    return answer

def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1