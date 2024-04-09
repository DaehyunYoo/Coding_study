# 음식물 피하기
# 백준1743

from collections import deque

N, M, K = map(int, input().split())

graph = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 음식물 좌표 1 입력
for _ in range(K):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

result = 0

def BFS(i, j):
    global cnt
    
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny] == 1: # 해당 노드가 1인 경우만 밟기
                    visited[nx][ny] = True
                    cnt += 1
                    queue.append((nx, ny))
    
    return cnt
                    

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = 0
            cnt = BFS(i, j)
            result = max(result, cnt)

print(result + 1)
