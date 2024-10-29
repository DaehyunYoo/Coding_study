# 배열 조각하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181893

def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]
    return arr

def solution(arr, query):
    for idx, val in enumerate(query):
        if idx % 2 == 0:
            arr = arr[:val+1]
        else:
            arr = arr[val:]
    return arr