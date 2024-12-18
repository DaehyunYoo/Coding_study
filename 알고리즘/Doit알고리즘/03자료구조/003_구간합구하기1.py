# 구간 합 구하기 1
# 백준 11659
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 누적합 배열
sums = [0]
cumulative = 0
for i in nums:
    cumulative += i
    sums.append(cumulative)

for j in range(M):
    start, end = map(int, input().split())
    print(sums[end] - sums[start-1])
    