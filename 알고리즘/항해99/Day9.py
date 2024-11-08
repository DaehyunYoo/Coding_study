import sys
from collections import deque
input = sys.stdin.readline

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def BFS(start_x, start_y, destination_x, destination_y, I):
    queue = deque()
    queue.append((start_x, start_y))
    graph = [[0] * I for _ in range(I)]
    graph[start_x][start_y] = 1
    while queue:
        x, y = queue.popleft()
        if x == destination_x and y == destination_y:
            return graph[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

T = int(input())

for _ in range(T):
    I = int(input())
    start_x, start_y = map(int, input().split())
    destination_x, destination_y = map(int, input().split())
    print(BFS(start_x, start_y, destination_x, destination_y, I))
