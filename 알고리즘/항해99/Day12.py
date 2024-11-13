# 항해 Day 12
# 백준 7569
from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

# 먼저 3차원 배열 초기화
graph = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

# 값 입력 받기
for i in range(H):
    for j in range(N):
        graph[i][j] = list(map(int, input().split()))
        

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

def BFS():
    queue = deque()
    # 입력이 완료된 후 익은 토마토 위치를 큐에 추가
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 1:
                    queue.append((i, j, k))
    
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz, nx, ny))

# BFS 실행
BFS()

# 결과 확인
day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:  # 익지 않은 토마토가 있다면
                print(-1)
                exit()
            day = max(day, graph[i][j][k])

# 처음 토마토가 1이었으므로 실제 일수는 최댓값 - 1
print(day - 1)