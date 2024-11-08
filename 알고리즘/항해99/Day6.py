# 항해99 6일차
# 백준 2805번 나무 자르기

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 나무의 수, 집에 가져가려는 나무의 길이
tree = list(map(int, input().split())) # 각 나무의 높이

answer = 0 # 최종 답
left = 0
right = 10**9

while left <= right:
    mid = (left + right) // 2
    result = 0
    
    for i in tree:
        if i > mid:
            result += i - mid
            
            if result > M: # result가 M보다 크면 더 이상 계산할 필요 없음
                break
            
            
    if result >= M: # result가 M보다 크거나 같으면 더 높이를 올려야 함
        answer = mid
        left = mid + 1 
    else: # result가 M보다 작으면 더 낮춰야 함
        right = mid - 1
        
print(answer)