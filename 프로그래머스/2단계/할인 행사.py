# 할인 행사
# https://school.programmers.co.kr/learn/courses/30/lessons/131127

from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = dict(zip(want, number))
    
    for i in range(len(discount)-9):
        sales = Counter(discount[i:i+10])
        if sales == dic:
            answer += 1
        
    return answer