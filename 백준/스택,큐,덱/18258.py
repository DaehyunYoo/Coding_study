# 큐 2
# 18258

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()

for i in range(N):
    lst = list(input().split())
    
    if lst[0] == 'push':
        queue.append(lst[1])
    
    elif lst[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:

            print(queue.popleft())
    elif lst[0] == 'size':
        print(len(queue))
        
    elif lst[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
            
    elif lst[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            
    elif lst[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])