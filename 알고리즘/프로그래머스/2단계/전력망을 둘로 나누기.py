# 전력망을 둘로 나누기

from collections import deque

def solution(n, wires):
    result = 0
    graph = [[0] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def BFS(start):
        visited = [False] * (n+1)
        queue = deque([start])
        visited[start] = True
        cnt = 1
        
        while queue:
            s = queue.popleft()
            for i in graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    cnt += 1
        return cnt
    
    result = n
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        result = min(abs(BFS(a) - BFS(b)), result)
        
        graph[a].append(b)
        graph[b].append(a)
        
    return result
        
    return answer