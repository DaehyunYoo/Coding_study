# 배열 만들기 3
# https://school.programmers.co.kr/learn/courses/30/lessons/181895

def solution(arr, intervals):
    answer = []
    a1, b1 = intervals[0]
    a2, b2 = intervals[1]
    answer = arr[a1:b1+1] + arr[a2:b2+1]
    return answer

def solution(arr, intervals):
    answer = []
    for a,b in intervals: answer+=arr[a:b+1]
    return answer