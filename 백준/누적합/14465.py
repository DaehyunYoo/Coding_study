# 소가 길을 건너간 이유 5
# 14465

'''
# 시간초과 코드

N, K, B = map(int, input().split())

lst = [0] * N
for i in range(B):
    a = int(input())
    lst[a-1] = 1

result = []
# 누적합 계산
for i in range(0, N-K+1):
    result.append(sum(lst[i:i+K]))

print(min(result))
'''

N, K, B = map(int, input().split())

# 각 램프의 상태를 나타내는 리스트 초기화
lst = [0] * N
for i in range(B):
    a = int(input())
    lst[a-1] = 1

# 첫 번째 윈도우의 깨진 램프 수 계산
current_broken = sum(lst[:K])
min_broken = current_broken

# 슬라이딩 윈도우를 이용해 각 위치에서의 깨진 램프 수 계산
for i in range(1, N-K+1):
    # 새 윈도우에서 맨 왼쪽 램프를 제거하고, 맨 오른쪽 램프를 추가
    current_broken = current_broken - lst[i-1] + lst[i+K-1]
    # 최소 깨진 램프 수 갱신
    if current_broken < min_broken:
        min_broken = current_broken

print(min_broken)
