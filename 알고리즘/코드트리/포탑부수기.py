# 포탑부수기
# https://www.codetree.ai/training-field/frequent-problems/problems/destroy-the-turret/description?page=1&pageSize=20

import sys
import copy
from collections import deque

# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

N, M, K = map(int, input().split())

tower = [list(map(int, input().split())) for _ in range(N)]

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

drr = [0, 1, 0, -1, 1, 1, -1, -1]
dcc = [1, 0, -1, 0, 1, -1, -1, 1]

attacker_his = [[0] * M for _ in range(N)]
    

# 공격자 선정
def select_attacker():
    global visited, tower
    
    power = 5001 # min을 찾아야하기 때문에 max보다 큰 값
    ar = ac = 0 # 선택된 공격자 위치 초기화
    # min
    for i in range(N):
        for j in range(M):
            if tower[i][j] > 0 and tower[i][j] < power:
                ar, ac = i, j
                power = tower[i][j]
            elif tower[i][j] == power:
                # 최근에 공격한 포탑
                if attacker_his[i][j] > attacker_his[ar][ac]: # 최근이면 값이 더 큼
                    ar, ac = i, j
                elif attacker_his[i][j] == attacker_his[ar][ac]: # 같으면 더 비교
                    if i + j > ar + ac:
                        ar, ac = i, j
                    elif i + j == ar + ac: # 행과 열의 합이 같다면 더 비교
                        if j > ac: # 열이 더 큰게 공격자로 선정
                            ar, ac = i, j
    
    visited[ar][ac] = True
    attacker_his[ar][ac] = turn + 1 # 공격 횟수 추가
    tower[ar][ac] += (M+N) # 공격력 증가
    
    return (ar, ac)

# 공격 대상 선정
def target(attacker):
    global visited, tower, attacker_his
    
    # 공격자(attacker)는 공격 대상에서 제외
    # max
    power = 0 # 0보다는 커야함. 
    tr = tc = 0 # target 위치 초기화
    
    for i in range(N):
        for j in range(M):
            if tower[i][j] > 0  and tower[i][j] > power and (i, j) != attacker:
                power = tower[i][j] # power update
                tr, tc = i, j # 위치 업데이트
            elif tower[i][j] == power and (i, j) != attacker:
                # 공격한지 가장 오래된 포탑
                if attacker_his[i][j] < attacker_his[tr][tc]:
                    tr, tc = i, j
                elif attacker_his[i][j] == attacker_his[tr][tc]:
                    # 행과 열의 합이 가장 작은 포탑
                    if i + j < tr + tc:
                        tr, tc = i, j
                    elif i + j == tr + tc:
                        # 열이 가장 작은 포탑
                        if j < tc:
                            tr, tc = i, j
    
    target = (tr, tc)
    visited[tr][tc] = True
    
    # 공격
    if not laser(attacker, target): # 레이저 공격 아니면 
        bomb(attacker, target) # 포탄 공격
    return

def laser(attacker, target):
    global visited, tower
    laser_visited = [[False] * M for _ in range(N)]
    laser_visited[attacker[0]][attacker[1]] = True
    queue = deque([(attacker, [])])

    while queue:
        (r, c), route = queue.popleft()

        for i in range(4):
            newr, newc = r + dr[i], c + dc[i]
            if 0 <= newr < N and 0 <= newc < M and not laser_visited[newr][newc] and tower[newr][newc] > 0:
                if (newr, newc) == target:
                    power = tower[attacker[0]][attacker[1]]
                    tower[target[0]][target[1]] = max(0, tower[target[0]][target[1]] - power)
                    for rr, cc in route:
                        tower[rr][cc] = max(0, tower[rr][cc] - power // 2)
                        visited[rr][cc] = True
                    return True
                route.append((newr, newc))
                laser_visited[newr][newc] = True
                queue.append(((newr, newc), route[:]))  # Shallow copy of the route
    return False


# 포탄 공격
def bomb(attacker, target):
    # attack visited
    global visited, tower
    power = tower[attacker[0]][attacker[1]]
    tower[target[0]][target[1]] = max(0, tower[target[0]][target[1]] - power)
    
    for i in range(8):
        newr, newc = (target[0] + drr[i]) % N, (target[1] + dcc[i]) % M
        
        if tower[newr][newc] > 0 and (newr, newc) != attacker:
            tower[newr][newc] = max(0, tower[newr][newc] - power // 2)
            visited[newr][newc] = True
    
    return

# 포탑정비

def repair():
    # 부서지지않은 포탑이 하나남으면 중지
    global tower
    
    cnt = 0
    for i in range(N):
        cnt += tower[i].count(0)
        for j in range(M):
            if tower[i][j] > 0 and not visited[i][j]:
                tower[i][j] += 1
    
    if cnt > M*N - 1:
        return False
    return True


for turn in range(K):
    visited = [[False] * M for _ in range(N)]
    attacker = select_attacker()
    target(attacker)
    if not repair():
        break

# 결과 출력 부분
ans = 0
for i in range(N):
    for j in range(M):
        ans = max(tower[i][j], ans)
print(ans)      