# N개의 최소 공배수
# https://school.programmers.co.kr/learn/courses/30/lessons/12953

import math

def solution(arr):
    answer = arr[0]
    for i in arr:
        answer = (i * answer) // math.gcd(i, answer)

    return answer