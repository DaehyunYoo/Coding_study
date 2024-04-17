# 이분 그래프
# 백준 1707번

from collections import deque

def BFS(v, group):
    queue = deque()
    queue.append(v)
    visited[v] = group
    
    while queue:
        nx = queue.popleft()
        
        for i in graph[nx]:
            if not visited[i]:
                # visited[i] = True
                queue.append(i)
                visited[i] = -1 * visited[nx]
            elif visited[i] == visited[nx]:
                return False
    return True

for _ in range(int(input())): # K
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
                    
    for i in range(1, V+1):
        if not visited[i]:
            result = BFS(i, 1) # 
            if not result:
                break

    print('YES' if result else 'NO')