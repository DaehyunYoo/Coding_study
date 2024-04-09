# 연결 요소의 개수 
# 백준 11724 

from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


# BFS 함수 정의
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    
    while queue:
        now_Node = queue.popleft() # 현재 노드
        for i in graph[now_Node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        BFS(i)
        cnt += 1

print(cnt)
        