# 나머지 합 구하기
# 백준 10986
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 누적 합의 나머지를 저장
remain = [0] * M
prefix = 0

# 각 누적 합을 M으로 나눈 나머지를 계산
for i in range(N):
    prefix += nums[i]
    remain[prefix % M] += 1

# 나머지가 0인 경우를 더함
answer = remain[0]

# 같은 나머지를 가진 구간의 조합을 계산
for i in range(M):
    if remain[i] > 1:
        answer += (remain[i] * (remain[i] - 1)) // 2

print(answer)