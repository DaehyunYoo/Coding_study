# 게임 맵 최단거리

from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)  # 행의 수
    m = len(maps[0])  # 열의 수

    
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((0,0))

    visited[0][0] = True
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and maps[ny][nx] == 1:
                    visited[ny][nx] = True
                    maps[ny][nx] = maps[y][x] + 1
                    queue.append((ny, nx))
    
    if maps[m-1][n-1] == 1:
        return -1
    else:
        return maps[m-1][n-1]
    
    return answer