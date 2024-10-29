# 음식물 피하기
# 백준 1743번

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
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    cnt = 1  # 시작 지점 포함하여 카운트 시작
    
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]  # 수정: nx 계산 시 x 사용
            ny = y + dy[k]  # 수정: ny 계산 시 y 사용
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    cnt += 1
                    queue.append((nx, ny))
    return cnt
                    

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = BFS(i, j)  # BFS 함수에서 cnt를 초기화하므로 별도 초기화 불필요
            result = max(result, cnt)

print(result)  # 마지막 결과 출력 수정
