# 전투
# 백준 1303번
from collections import deque

N, M = map(int, input().split())

A = [list(input()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
        
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(i, j, team):
    cnt = 0
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    
    while queue:
        i, j = queue.popleft()
        cnt += 1 # 개수 추가
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            
            if x >= 0 and y >= 0 and x < M and y < N:
                if A[x][y] == team and not visited[x][y]:
                    visited[x][y] = True
                    queue.append((x, y))
        
    return cnt

white, black = 0, 0

for i in range(M):
    for j in range(N):
        if A[i][j] == 'W' and not visited[i][j]:
            white += BFS(i, j, 'W') ** 2
        elif A[i][j] == 'B' and not visited[i][j]:
            black += BFS(i, j, 'B') ** 2
            
print(white, black)