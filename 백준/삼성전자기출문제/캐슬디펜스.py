# # 캐슬 디펜스
# # https://www.acmicpc.net/problem/17135

# from collections import deque
# from copy import deepcopy
# from itertools import combinations

# N, M, D = map(int, input().split())  # 격자판 행, 열, 궁수 사거리
# graph = [list(map(int, input().split())) for _ in range(N)]  # 격자판

# answer = 0  # 최대 적 수

# # 궁수 공격 방향 수정: 위, 왼쪽, 오른쪽 순으로 탐색
# dx = [0, -1, 0]
# dy = [-1, 0, 1] 

# # BFS 수정: 각 궁수 위치에서 궁수 공격 로직
# def BFS(archor):
#     A = deepcopy(graph)  # 격자판 복사
#     cnt = 0
    
#     for row in range(N, 0, -1):  # 적 전진(실제로는 궁수가 위로 올라가는 것으로 처리)
#         die = set()  # 죽일 적의 위치 (중복 제거)
        
#         for k in archor:  # 궁수 3명
#             queue = deque([(row, k, 0)])  # 시작 위치와 거리
            
#             while queue:
#                 y, x, d = queue.popleft()
#                 if 0 <= y < N and 0 <= x < M and d <= D:
#                     if A[y][x] == 1:
#                         die.add((y, x))  # 적 발견 시 추가
#                         break  # 최소 거리의 적을 찾으면 중단
#                     if d < D:  # 사거리 안에 있으면
#                         for di in range(3):
#                             nx = x + dx[di]
#                             ny = y + dy[di]
#                             if 0 <= ny < N and 0 <= nx < M:
#                                 queue.append((ny, nx, d + 1))
                        
#         for y, x in die:  # 적 제거
#             if A[y][x] == 1:
#                 cnt += 1
#                 A[y][x] = 0

#     return cnt

# for archor in combinations(range(M), 3):  # 가능한 모든 궁수의 위치 조합
#     answer = max(answer, BFS(archor))
    
# print(answer)  # 최대 적 제거 수 출력
