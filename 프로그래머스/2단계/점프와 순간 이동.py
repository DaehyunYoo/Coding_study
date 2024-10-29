# 점프와 순간 이동
# https://school.programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 0
    while n != 1:
        if n % 2 != 0:
            ans += 1
            n //= 2
        else:
            n //= 2
            
    return ans + 1