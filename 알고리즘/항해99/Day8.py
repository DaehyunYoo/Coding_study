# 항해 99 Day 8
# 백준 2644번 촌수계산

import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
visited = [0] * (n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def DFS(v):
    if v == b: # 도착점이 해당 번호라면
        return visited[v]
    
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = visited[v] + 1
            result = DFS(i)
            if result != -1:
                return result
    
    return -1

visited[a] = 0

print(DFS(a))
            