# 글자 지우기
# https://school.programmers.co.kr/learn/courses/30/lessons/181900

def solution(my_string, indices):
    answer = ''
    for idx, val in enumerate(my_string):
        if idx not in indices:
            answer += val
    return answer

def solution(my_string, indices):
    my_string = list(my_string)
    for i in sorted(indices, reverse=True):
        del my_string[i]
    return ''.join(my_string)