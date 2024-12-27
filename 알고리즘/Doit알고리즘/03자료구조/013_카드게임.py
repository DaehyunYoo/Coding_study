# 카드 게임
# 백준 2164

from collections import deque

N = int(input())

lst = deque()
for i in range(1, N+1):
    lst.append(i)


while len(lst) > 1:
    lst.popleft()
    a = lst[0]
    lst.append(a)
    lst.popleft()

print(*lst)