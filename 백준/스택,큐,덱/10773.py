# 제로
# 10773

import sys
input = sys.stdin.readline

K = int(input())
sum_list = []

for _ in range(K):
    num = int(input())
    if num != 0:
        sum_list.append(num)
    else:
        sum_list.pop()

print(sum(sum_list))