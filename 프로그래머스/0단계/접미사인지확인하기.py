# 접미사인지 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181908

def solution(my_string, is_suffix):
    answer = 0
    lst = []
    for i in range(len(my_string)):
        lst.append(my_string[i:])
    if is_suffix in lst:
        answer = 1
    else:
        answer = 0
    return answer

def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))