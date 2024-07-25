# 트리의 부모 찾기
# 11725
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
parent = [-1] * (N+1)

def DFS(v):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            parent[i] = v
            DFS(i)

DFS(1)

for i in range(2, N+1):
    print(parent[i])