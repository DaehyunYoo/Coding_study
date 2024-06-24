# DFS와 BFS
# 1260
 
from collections import deque

N, M, V = map(int, input().split())
graph = [[] * (N+1) for _ in range(N+1)]

# 인접노드 리스트
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()


# 방문 여부 체크
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

# 결과 창
dfs_result, bfs_result = [], []

# 1. DFS

def dfs(graph, v, visited):
    
    visited_dfs[v] = True
    # print(v, end = ' ')
    dfs_result.append(v)
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, V, visited_dfs)

# 2. BFS

def bfs(graph, start, visited):
    
    queue = deque([start])
    visited_bfs[start] = True
    
    while queue:
        v = queue.popleft()
        # print(v, end = ' ')
        bfs_result.append(v)
        
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited[i] = True
                
bfs(graph, V, visited_bfs)

print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))