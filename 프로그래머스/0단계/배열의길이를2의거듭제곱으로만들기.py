# 배열의 길이를 2의 거듭제곱으로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181857

def solution(arr):
    answer = 0 
    k = len(arr)
    while k > 1:
        k = k / 2 
        answer += 1    
    return arr + [0]*(2**answer - len(arr))