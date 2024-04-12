# 왕실의 기사 대결
#  https://www.codetree.ai/training-field/frequent-problems/problems/royal-knight-duel/description?page=1&pageSize=20&tags=BFS

from collections import deque

# 전역 변수 정의
Max_N = 31 # 기사 최대 수
Max_L = 41 # 체스판 최대 크기

# 상 우 하 좌
dx = [-1, 0, 1, 0] # 행 변화령 
dy = [0, 1, 0, -1] # 열 변화량

info = [[0 for _ in range(Max_L)] for _ in range(Max_L)] # 체스판 정보: 빈칸, 함정, 벽
bef_k = [0 for _ in range(Max_N)] # 각 기사의 초기 최대 체력
r = [0 for _ in range(Max_N)] # 각 기사의 현재 행 위치
c = [0 for _ in range(Max_N)] # 각 기사의 현재 열 위치
h = [0 for _ in range(Max_N)] # 각 기사의 높이
w = [0 for _ in range(Max_N)] # 각 기사의 너비
k = [0 for _ in range(Max_N)] # 각 기사의 현재 체력
nr = [0 for _ in range(Max_N)] # 이동 후 각 기사의 잠재적 행 위치
nc = [0 for _ in range(Max_N)] # 이동 후 각 기사의 잠재적 열 위치
dmg = [0 for _ in range(Max_N)] # 각 기사가 이동 중 받는 피해량
visited = [False] * Max_N # 이동 여부 플래그


def try_movement(idx, dir):
    queue = deque()
    is_pos = True
    
    # 이동 초기화: 모든 기사에 대한 피해, 이동 여부 초기화
    for i in range(1, N + 1):
        dmg[i] = 0
        visited[i] = False
        nr[i] = r[i]
        nc[i] = c[i]
        
    queue.append(idx)
    visited[idx] = True
    
    while queue:
        x = queue.popleft()
        
        nr[x] += dx[dir]
        nc[x] += dy[dir]
        
        # 이동 범위 체크: 벽 or 체스판 초과시 이동 불가
        if nr[x] < 1 or nc[x] < 1 or nr[x] + h[x] - 1 > L or nc[x] + w[x] - 1 > L:
            return False
        
        # 충돌 검사: 이동 경로 내 함정 or 벽
        for i in range(nr[x], nr[x] + h[x]):
            for j in range(nc[x], nc[x] + w[x]):
                if info[i][j] == 1:
                    dmg[x] += 1
                if info[i][j] == 2:
                    return False
                
        
        # 다른 기사와의 충돌 시 같이 이동 처리
        for i in range(1, N+1):
            if visited[i] or k[i] <= 0: # visited[]
                continue
            if r[i] > nr[x] + h[x] - 1 or nr[x] > r[i] + h[i] - 1:
                continue
            if c[i] > nc[x] + w[x] - 1 or nc[x] > c[i] + w[i] - 1:
                continue
            
            visited[i] = True
            queue.append(i)
        
    dmg[idx] = 0
    
    return True

# 기사 이동
def move_knight(idx, move_dir):
    # 체력이 0인 기사는 이동 불가(사라짐)
    if k[idx] <= 0: 
        return 
    
    # 이동 가능한 경우 위치 및 체력 업데이트
    if try_movement(idx, move_dir):
        for i in range(1, N+1):
            r[i] = nr[i]
            c[i] = nc[i]
            k[i] -= dmg[i]
            

# 메인
L, N, Q = map(int, input().split())

# 체스판 정보 입력
for i in range(1, L+1): 
    info[i][1:] = map(int, input().split())

# 초기 기사 정보 입력
for i in range(1, N+1):
    r[i], c[i], h[i], w[i], k[i] = map(int, input().split())
    bef_k[i] = k[i]

# 왕의 명령 정보 입력
for _ in range(Q):
    # 기사 번호(idx), 방향(d)
    idx, d = map(int, input().split())
    move_knight(idx, d)

# 결과 출력
result = sum([bef_k[i] - k[i] for i in range(1, N+1) if k[i] > 0])
print(result)