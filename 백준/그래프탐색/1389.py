# 케빈 베이컨의 6단계 법칙
# 백준 1389


from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    dist[v] = 0
    
    while queue:
        now_Node = queue.popleft()
        for i in graph[now_Node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                dist[i] = dist[now_Node] + 1
            

min_kevin_bacon = 1e9
min_person = -1

for i in range(1, N+1):
    # i를 시작점으로 하는 BFS
    # 각 노드까지의 최단 거리를 구해서 합하기
    visited = [False] * (N+1)
    dist = [-1] * (N+1)
    BFS(i)
    kevin_bacon = sum(dist)
    
    if min_kevin_bacon > kevin_bacon:
        min_kevin_bacon = kevin_bacon
        min_person = i

print(min_person)