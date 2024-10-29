# # 잃어버린 괄호
# # 1541

import sys
input = sys.stdin.readline

equation = input().split('-')

num = []

for i in equation:
    cnt = 0
    for j in i.split('+'):
        cnt += int(j)
    num.append(cnt)

result = num[0]
for i in num[1:]:
    result -= i

print(result)
