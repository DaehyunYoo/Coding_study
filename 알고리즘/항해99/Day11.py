import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

S = int(input()) # 곰곰이 갯수
fans = set(map(int, input().split())) # 팬클럽 곰곰이 번호를 set으로 변환
visited = [False] * (N+1)

answer = False # 팬을 만나지 않는 경로가 있는지 없는지에 대한 변수

def DFS(v):
    global visited, graph, answer
    if v in fans:  # 현재 정점에 팬이 있으면 리턴
        return 
    
    # 더 이상 갈 수 있는 곳이 없고 팬을 만나지 않았다면 answer를 True로
    if not graph[v]:
        answer = True
        return 
    
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i)
    visited[v] = False # 백트래킹
    
if 1 in fans:  # 시작점에 팬이 있는 경우
    print("Yes")
else:
    DFS(1)
    if answer:  # 팬을 만나지 않는 경로가 있는 경우
        print("yes")
    else:  # 모든 경로에서 팬을 만나는 경우
        print("Yes")