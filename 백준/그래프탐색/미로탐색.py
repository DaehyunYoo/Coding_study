# 백준 미로탐색
# https://www.acmicpc.net/problem/2178

from collections import deque

N, M = map(int, input().split())
A = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(N):
    numbers = list(input())
    for j in range(M):
        A[i][j] = int(numbers[j])

# print(A)

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    
    while queue:
        now_Node = queue.popleft()
        # print(now_Node) # 현재 노드 = 현재 노드의 x, y 좌표
        for k in range(4): # 상하좌우
            x = now_Node[0] + dx[k] # x는 현재 노드의 x좌표에 dx[k]를 더한 값
            y = now_Node[1] + dy[k] 

            if x>= 0 and y>=0 and x<N and y<M:
                if A[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    print(f'A[now_Node[0]][now_Node[1]:{A[now_Node[0]][now_Node[1]]}')
                    A[x][y] = A[now_Node[0]][now_Node[1]] + 1 # +1을 해주는 이유는 이전 노드에서 1을 더해주는 것이다.
                    queue.append((x, y))

BFS(0, 0)
print(A[N-1][M-1])