# A로 B만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/120886

def solution(before, after):
    before=sorted(before)
    after=sorted(after)
    if before==after:
        return 1
    else:
        return 0