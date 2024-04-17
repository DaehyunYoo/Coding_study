# 배열의 원소 삭제하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181844

def solution(arr, delete_list):
    answer = []
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr