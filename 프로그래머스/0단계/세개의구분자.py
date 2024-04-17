# 세 개의 구분자
# https://school.programmers.co.kr/learn/courses/30/lessons/181862

def solution(myStr):
    answer = []
    for i in ['a', 'b', 'c']:
        myStr = myStr.replace(i, ' ')

    answer = myStr.split()

    if not answer:
        answer = ["EMPTY"]
    return answer