# 숨어있는 숫자의 덧셈 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120864

def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ')
    my_string = my_string.split()
    for j in my_string:
        answer += int(j)
    return answer