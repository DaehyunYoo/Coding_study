# 항해 99 Day 3
# 프로그래머스 입국심사
## 이분탐색을 통해서 총 걸리는 시간을 점점 좁혀나가는 형식으로 푸는 문제

def solution(n, times):
    answer = 0
    # right는 가장 오래 걸리는 심사관이 모든 사람을 심사하는 경우로 나올 수 있는 최대 시간
    left, right = 1, max(times) * n 
    
    while left < right:
        mid = (left + right) // 2
        people = 0
        
        # 심사자가 n명이기 때문에 각 심사관이 mid 시간동안 심사할 수 있는 사람 수를 구해서 더함
        for i in times:
            people += mid // i
            # 만약 mid 시간동안 심사한 사람이 n명보다 크다면 break
            if people > n:
                break
        # 만약 mid 시간동안 심사한 사람이 n명보다 크거나 같다면 answer에 mid를 저장하고 right를 mid - 1로 변경
        if people >= n:
            answer = mid 
            right = mid - 1
        else:
            left = mid + 1
            
    return answer