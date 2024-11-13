# 밤양갱
# 백준 31926
import sys
input = sys.stdin.readline

n = int(input())
answer = 10  # 초기값 (n=1일 때의 답)

bomb = 1  # 기준값 (2의 거듭제곱)
while n >= bomb * 2:
    answer += 1
    bomb *= 2

print(answer)