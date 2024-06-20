# 귤 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/138476

import collections

def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)
    cnt = sorted(cnt.values(), reverse=True)
    
    for i in cnt:
        answer += 1
        k -= i
        if k <= 0:
            break
    return answer