# 2864
# 5와 6의 차이

import sys
input = sys.stdin.readline

A, B = map(str, input().split())

min_sum = int(A.replace('6', '5')) + int(B.replace('6', '5'))
max_sum = int(A.replace('5', '6')) + int(B.replace('5', '6'))

print(f'{min_sum} {max_sum}')