# 백준 1374
# 강의실

# 백준 1374
# 강의실

import sys
input = sys.stdin.readline

N = int(input())
time = []

# 시작 시간과 종료 시간을 따로 저장하면서 시작은 1로, 종료는 -1로 표시
for _ in range(N):
    num, start, end = map(int, input().split())
    time.append((start, 1))   # 시작 시간
    time.append((end, -1))    # 종료 시간

# 시간 순으로 정렬, 같은 시간이면 종료를 먼저 처리(-1이 1보다 앞으로)
time.sort()

curr_rooms = 0  # 현재 사용 중인 강의실
max_rooms = 0   # 필요한 최대 강의실

for t, v in time:
    curr_rooms += v  # 시작이면 +1, 종료면 -1
    max_rooms = max(max_rooms, curr_rooms)

print(max_rooms)