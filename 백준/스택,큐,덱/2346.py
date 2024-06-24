# 풍선 터뜨리기
# 2346

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

queue = deque(enumerate(map(int, input().split())))
result = []

while queue:
    idx, now_turn = queue.popleft()
    result.append(idx+1)
    
    if now_turn > 0:
        queue.rotate(-(now_turn - 1))
    else:
        queue.rotate(-now_turn)

print(' '.join(map(str, result)))