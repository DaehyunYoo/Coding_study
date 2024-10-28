# 할 일 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/181885

def solution(todo_list, finished):
    answer = []
    for idx, val in enumerate(finished):
        print(val)
        if val == False:
            answer.append(todo_list[idx])
    return answer

def solution(todo_list, finished):
    answer = []
    for i, j in zip(todo_list, finished):
        if j == False:
            answer.append(i)
    return answer