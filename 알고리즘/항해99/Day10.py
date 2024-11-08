from collections import deque
import sys

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# 단방향 그래프 생성
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)  # 단방향으로만 추가

visited = [-1] * (N + 1)  # 방문 배열을 거리 저장 용도로 활용

def BFS(start):
    queue = deque([start])
    visited[start] = 0  # 시작 도시까지의 거리는 0
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            # 방문하지 않은 도시인 경우
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                queue.append(i)
    
    # 거리가 K인 도시 찾기
    check = False
    for i in range(1, N + 1):
        if visited[i] == K:
            print(i)
            check = True
    
    if not check:
        print(-1)

BFS(X)