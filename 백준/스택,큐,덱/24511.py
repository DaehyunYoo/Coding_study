# queuestack
# 24511

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

result = deque()

for i in range(N):
    if A[i] == 0:
        result.appendleft(B[i])

for j in range(M):
    result.append(C[j])
    print(result.popleft(), end = ' ')