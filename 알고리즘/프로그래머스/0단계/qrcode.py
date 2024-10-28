# qr code
# https://school.programmers.co.kr/learn/courses/30/lessons/181903

def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
        else:
            continue
    return answer

def solution(q, r, code):
    return code[r::q]