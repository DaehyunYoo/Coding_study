import numpy as np

# 시험 본 과목의 개수
N = int(input())

# 현재시험 점수
score = list(map(int, input().split()))

# 최대 점수 
M = max(score)

# 새로운 점수 계산
new_score = []
for new_score in score:
    new_score.append(score/M*100)

test_avg = sum(new_score)/N
print(test_avg)
