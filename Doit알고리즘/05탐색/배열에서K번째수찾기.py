# 배열에서 K번째 수 찾기
## 백준 1300

N = int(input())
K = int(input())
start = 1
end = K
ans = 0

# 이진 탐색
while start < end:
    middle = int((start + end) / 2)
    cnt = 0
    
    for i in range(1, N+1):
        cnt += min(int(middle / i), N) 
    if cnt < K:
        start = middle + 1
    else:
        ans = middle
        end = middle - 1
        
print(ans)