# DFS 기본 코드

def DFS(graph, v, visited): # graph: 그래프, v: 현재 노드, visited: 방문한 노드
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = '') # 방문한 노드 출력
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]: # 방문하지 않은 노드라면 
            # print(f'방문하지 않은 노드: {i}')
            DFS(graph, i, visited) 
        

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [], # 0번 노드는 없으므로 비워둠
    [2, 3, 8], # 1번 노드와 연결된 노드들
    [1, 7], 
    [1, 4, 5], 
    [3, 5], 
    [3, 4], 
    [7], 
    [2, 6, 8], 
    [1, 7] 
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9 # 0번 노드는 없으므로 9개의 False로 초기화

# 정의된 DFS 함수 호출
DFS(graph, 1, visited) # 시작 노드: 1