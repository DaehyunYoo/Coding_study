import sys
input = sys.stdin.readline

N, K = map(int, input().split())  

coins = []
for _ in range(N):
    coins.append(int(input())) 

cnt = 0  

for i in range(N - 1, -1, -1):
    if coins[i] <= K:  # 현재 동전이 K 이하일 때만 계산을 수행
        cnt += K // coins[i]  # 동전을 사용할 수 있는 최대 횟수를 더하기
        K %= coins[i]  # 남은 금액을 업데이트

    if K == 0:  # 남은 금액이 0이 되면 모든 계산 중단
        break

print(cnt) 
