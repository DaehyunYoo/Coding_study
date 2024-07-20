# 수들의 합 2
# 2003

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

start = 0 # 시작점
end = 0 # 끝점
sum = A[0] 

count = 0
while True:
    # 현재 구간이 합이 M인지 확인
    if sum == M:
        count += 1
    
    # 구간을 업데이트
    if sum >= M:
        start += 1
        sum -= A[start - 1]
    else: # sum < M
        if end == N - 1:
            break
        end += 1
        sum += A[end]
        
print(count)