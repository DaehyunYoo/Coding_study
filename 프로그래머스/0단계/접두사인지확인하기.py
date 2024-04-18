# 접두사인지 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181906

def solution(my_string, is_prefix):
    answer = 0
    lst = []
    for i in range(len(my_string)):
        lst.append(my_string[:i])
    if is_prefix in lst:
        answer = 1
    else:
        answer = 0
    return answer

def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))