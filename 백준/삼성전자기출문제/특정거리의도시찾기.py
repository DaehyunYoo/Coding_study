# 삼성전자 기출문제
# 특정 거리의 도시 찾기
# 백준 18352번

from collections import deque

N, M, K, X = map(int, input().split())
A = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)
    
for i in range(N+1):
    A[i].sort()

visited = [False] * (N + 1)

distance = [0] * (N + 1) # 거리를 저장할 리스트

def BFS(v):
    result = []
    queue = deque([v]) # deque에 v를 넣어줌
    visited[v] = True
    distance[v] = 0
    while queue: # queue가 빌 때까지 반복
        now_Node = queue.popleft() # queue의 첫번째 원소를 빼서 now_Node에 저장
        for i in A[now_Node]: # now_Node와 연결된 노드들을 탐색
            if not visited[i]: 
                visited[i] = True
                queue.append(i) # queue에 i를 넣어줌
                print(queue)
                distance[i] = distance[now_Node] + 1 # 거리를 1씩 증가
                if distance[i] == K:
                    result.append(i)
    
    if len(result) == 0:
        print(-1)
    else:
        result.sort()
        for i in result:
            print(i, end='\n')

BFS(X)