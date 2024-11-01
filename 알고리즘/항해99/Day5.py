# 항해99 Day5
# 백준 24444번 알고리즘 수업 - 너비 우선 탐색

from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph= [[] for _ in range(N+1)]
visited = [0] * (N+1) 

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 오름차순 방문을 위한 정렬
for i in range(N+1):
    graph[i].sort()

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = 1 # 시작 정점의 방문 순서는 1
    cnt = 2 # 다음 방문할 정점의 순서는 2부터 시작
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]: # 아직 방문하지 않은 정점이면
                visited[i] = cnt # 현재 카운트를 방문 순서로 기록
                cnt += 1 # 다음 방문할 정점의 순서 증가
                queue.append(i)

BFS(graph, R, visited)

for i in range(1, N+1):
    print(visited[i])