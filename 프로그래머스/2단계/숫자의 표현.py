# 숫자의 표현
# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        sum = 0
        for j in range(i, n + 1):
            sum += j
            if sum == n:
                answer += 1
            elif sum > n:
                break
            else:
                continue
                    
    return answer