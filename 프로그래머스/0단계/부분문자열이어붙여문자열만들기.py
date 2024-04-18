# 부분 문자열 이어 붙여 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181911

def solution(my_strings, parts):
    answer = ''
    for idx, val in enumerate(parts):
        answer += my_strings[idx][val[0]:val[1]+1]

    return answer

def solution(my_strings, parts):
    answer = []
    for string, part in zip(my_strings, parts):
        i, j = part
        answer.append(string[i:j+1])
    return ''.join(answer)