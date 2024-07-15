# 피로도

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for i in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0
        
        for need, spend in i:
            if tmp >= need:
                tmp -= spend
                cnt += 1
        
        answer = max(answer, cnt)
    return answer