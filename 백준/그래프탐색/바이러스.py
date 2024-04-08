# 바이러스
# https://www.acmicpc.net/problem/2606

from collections import deque

# 컴퓨터 수 
N = int(input())

# 연결된 컴퓨터 쌍의 수
M = int(input())

# 그래프 초기화
A = [[] for _ in range(N+1)]

# 방문 기록 초기화
visited = [False] * (N+1)

for i in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

# print(A)

def BFS(v):
    queue = deque([v])
    visited[v] = True  # 시작 노드 방문 표시
    infected_count = 0  # 바이러스에 감염된 컴퓨터 수

    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                infected_count += 1  # 감염된 컴퓨터 수 증가

    return infected_count

infected_count = BFS(1)
print(infected_count)