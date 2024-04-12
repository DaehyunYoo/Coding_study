# 파이프 옮기기1
# 백준 17070
# https://www.acmicpc.net/problem/17070

"""
시간초과 코드

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

# 0: 길, 1: 벽
house = [list(map(int, input().split())) for _ in range(N)]

# (1,2)에서 시작
# (N,N)으로 이동

def function():
    queue = deque()
    queue.append((0, 1, 0))
    cnt = 0
    
    while queue:
        x, y, z = queue.popleft()
        if x == N-1 and y == N-1:
            cnt += 1
            continue
        
        # y축 이동(가로)
        if z == 0 or z == 2:
            if y+1 < N and house[x][y+1] == 0:
                queue.append((x, y+1, 0))
        
        # x축 이동(세로)
        if z == 1 or z == 2:
            if x+1 < N and house[x+1][y] == 0:
                queue.append((x+1, y, 1))
                
        # 대각선 이동
        if x+1 < N and y+1 < N:
            if house[x+1][y] == 0 and house[x][y+1] == 0 and house[x+1][y+1] == 0:
                queue.append((x+1, y+1, 2))
                
    return cnt

# 도착지점에 벽
if house[N-1][N-1] == 1:
    print(0)
else:
    print(function())
"""

# DFS 코드
# 시간 초과
n = int(input())
graph = [[] for _ in range(n)]
cnt = 0

# 그래프 정보 입력
for i in range(n):
    graph[i] = list(map(int, input().split()))


def DFS(position):
    global cnt
    
    x, y, z = position
    if x == n - 1 and y == n - 1:
        cnt += 1
        return
    
    # 대각선 이동
    if x + 1 < n and y + 1 < n: 
        if graph[x + 1][y + 1] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y] == 0:
            DFS((x + 1, y + 1, 2))
    
    # 세로 이동        
    if z == 0 or z == 2:
        if y + 1 < n:
            if graph[x][y + 1] == 0:
                DFS((x, y + 1, 0))
    
    # 가로 이동
    if z == 1 or z == 2:
        if x + 1 < n:
            if graph[x + 1][y] == 0:
                DFS((x + 1, y, 1))


DFS((0, 1, 0))

print(cnt)


# 정답 코드

import sys
input  = sys.stdin.readline
 
n = int(input())
G = [list(map(int,input().split())) for _ in range(n)]
 
dp = [[[0,0,0] for _ in range(n)] for _ in range(n+1)] # 가로 대각선 세로
 
dp[1][1] = [1,0,0]
 
 
for i in range(1,n+1):
    for j in range(1,n):
        if i==j==1:
            continue
        if G[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1] # 가로
            dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2] # 세로 
            if G[i][j-1] == G[i-1][j] == 0 :
                dp[i][j][1] = sum(dp[i-1][j-1]) # 대각선
 
 
 
print(sum(dp[-1][-1]))