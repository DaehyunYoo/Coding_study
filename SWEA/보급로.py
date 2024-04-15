# 보급로
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AV15QRX6APsCFAYD&categoryId=AV15QRX6APsCFAYD&categoryType=CODE&problemTitle=%EB%B3%B4%EA%B8%89%EB%A1%9C&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1&problemLevel=3%2C4&&&&&&&&&

# visited : 메모리 오류로 인해 사용하지 않음.
'''
메모리 오류 코드

from collections import deque

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    board = [list(map(int, list(input()))) for _ in range(N)]
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    result = [[float('inf')] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]  # 방문 배열 초기화
    
    def BFS(i, j):
        queue = deque()
        queue.append((i, j))
        result[i][j] = 0
        visited[i][j] = True  # 시작 지점 방문 표시
        
        while queue:
            x, y = queue.popleft()
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    visited[nx][ny] = True  
                # if 0 <= nx < N and 0 <= ny < N:
                    if result[x][y] + board[nx][ny] < result[nx][ny]:
                        result[nx][ny] = result[x][y] + board[nx][ny]
                        queue.append((nx, ny))
                        
    BFS(0, 0)
    print(f'#{test_case} {result[N-1][N-1]}')

'''
from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    
    # BFS
    N = int(input())
    graph = [list(map(int, list(input()))) for _ in range(N)]
    
    result = [[float('inf')] * N for _ in range(N)]
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    def BFS(i, j):
        queue = deque()
        queue.append((i,j))
        result[i][j]=0
        
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or ny<0 or nx>=N or ny>=N:
                    continue
                if result[x][y] + graph[nx][ny] < result[nx][ny]: 
                    result[nx][ny] = result[x][y] + graph[nx][ny]
                    queue.append((nx,ny))
    BFS(0,0)
    print(f'#{test_case} {result[N-1][N-1]}')
