# 평균 구하기
# 백준 1546

N = int(input())
scores = list(map(int, input().split()))

maximum = max(scores)
result = 0
for i in scores:
    result += ((i / maximum * 100))

print(result / N)
