# 리스트 자르기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181897

def solution(n, slicer, num_list):
    answer = []
    if n == 1:
        answer = num_list[0:slicer[1]+1]
    elif n == 2:
        answer = num_list[slicer[0]:]
    elif n == 3:
        answer = num_list[slicer[0]:slicer[1]+1]
    else:
        for i in num_list[slicer[0]:slicer[1]+1:slicer[2]] :
            answer.append(i)
    return answer