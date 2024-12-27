# 절대값 힙 구현하기
# 백준 11286

from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input())
queue = PriorityQueue()

for i in range(N):
    x = int(input())
    if x == 0:
        if queue.empty():
            print('0')
        else:
            temp = queue.get()
            print(str((temp[1])))
    else:
        queue.put((abs(x), x))