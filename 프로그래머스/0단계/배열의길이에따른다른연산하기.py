# 배열의 길이에 따른 다른 연산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181854

def solution(arr, n):

    if len(arr) % 2 != 0:
        for i in range(len(arr)):
            if i % 2 == 0:
                arr[i] += n

    else:
        for j in range(len(arr)):
            if j % 2 != 0:
                arr[j] += n

    return arr