X, Y = map(int, input().split())
Z = (Y * 100) // X  

# 승률이 99%이상이면 절대 바뀔 수 없음
if Z >= 99:
    print(-1)
else:
    # 이분 탐색
    left, right = 0, 10**9
    result = -1
    while left <= right:
        mid = (left + right) // 2
        new_X = X + mid
        new_Y = Y + mid
        new_Z = (new_Y * 100) // new_X
        
        if new_Z > Z:
            result = mid
            right = mid -1
        else:
            left = mid + 1
        
            
    print(result)