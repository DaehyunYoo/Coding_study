# 섬의 개수
# https://www.acmicpc.net/problem/4963

from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def BFS(x, y):
    # visited[x][y] = 1
    graph[x][y] = 0
    # queue = deque()
    # queue.append([(x, y)])
    queue = deque([(x, y)])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < H and 0 <= ny < W:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0: 
        break
    
    graph = []
    visited = [[0] * W for _ in range(H)]
    answer = 0
    
    for _ in range(H):
        graph.append(list(map(int, input().split())))
    
    for x in range(H):
        for y in range(W):
            if graph[x][y] == 1 and not visited[x][y]:
                BFS(x, y)
                answer += 1

    print(answer)
