# 백준 24479
# 알고리즘 수업 - 깊이 우선 탐색 1

import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)] # 0번이 있으니
visited = [0] * (N+1) # 방문 순서 저장

count = 1  # 방문 순서

def DFS(graph, v, visited):
    global count 
    visited[v] = count # 현재 정점에 방문 순서 저장
    
    for i in graph[v]: # 현재 정점과 연결된 모든 정점 확인
        if visited[i] == 0: # 만약 방문하지 않은 정점이라면
            count += 1 # 방문 순서 증가
            DFS(graph, i, visited) # DFS 재귀


for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 오름차순 방문을 위한 정렬
for i in range(N+1):
    graph[i].sort()
    
DFS(graph, R, visited)

for i in range(1, N+1):
    print(visited[i])