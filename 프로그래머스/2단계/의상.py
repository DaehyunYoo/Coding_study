# 의상
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    dic = {}
    for i in range(len(clothes)):
        value, key = clothes[i][0], clothes[i][1]
        if key in dic:
            dic[key].append(value)
        else:
            dic[key] = [value]
    
    for i in dic:
        print(len(dic[i])+1)
        answer *=int(len(dic[i])+1)

        
    return answer -1 

from collections import Counter

def solution(clothes):
    # Counter로 각 종류별 옷의 개수를 셉니다.
    count = Counter(category for _, category in clothes)
    
    # 각 종류의 옷의 개수에 1을 더하여 (해당 종류를 입지 않는 경우 포함) 계산합니다.
    answer = 1
    for num in count.values():
        answer *= (num + 1)

    # 모든 종류를 입지 않는 경우는 없으므로 1을 빼줍니다.
    return answer - 1
