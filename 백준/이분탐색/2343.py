# 기타레슨
# 2343

N, M = map(int, input().split())
lecture = list(map(int, input().split()))

left = max(lecture)
right = sum(lecture)
answer = -1

while left <= right:
    middle = (left + right) // 2 # 임시 블루레이 용량
    
    blueray_num = 1
    remain = middle
    
    for i in range(N):
        if remain < lecture[i]:
            blueray_num += 1
            remain = middle
        
        remain -= lecture[i]
        
    if blueray_num <= M:
        answer = middle    
        right = middle - 1 # [left, middle - 1]
    else:
        left = middle + 1 # [middle + 1, right]

print(answer)
        