# 예산
# 2512

N = int(input())

budget = list(map(int, input().split()))
total = int(input())

# 상한선 찾기
left = 0
right = max(budget)
answer = -1

while left <= right:
    middle = (left + right) // 2
    
    sum = 0
    for i in range(N):
        sum += min(middle, budget[i])
    
    if sum <= total:
        answer = middle
        left = middle + 1
    else:
        right = middle - 1
        
print(answer)