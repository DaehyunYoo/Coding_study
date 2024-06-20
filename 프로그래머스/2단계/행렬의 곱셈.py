# 행렬의 곱셈
# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for k in range(len(arr2[0])):
            for j in range(len(arr1[0])):
                answer[i][k] += arr1[i][j] * arr2[j][k]
    
    return answer