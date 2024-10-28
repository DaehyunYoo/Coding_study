# 이진 변환 반복하기
# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    cnt, zerocnt = 0, 0
    while s != '1':
        cnt += 1
        num = s.count('1')
        zerocnt += len(s) - num
        s = bin(num)[2:]
    return [cnt, zerocnt]