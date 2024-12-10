# 백준 2212
# 센서

import sys
input = sys.stdin.readline

N = int(input())
K = int(input()) # 집중국의 개수

# N개 센서의 좌표
sensors = list(map(int, input().split()))
sensors.sort() # 센서의 좌표를 정렬

dist = [] # 각 센서 사이의 거리

for i in range(1, N):
    dist.append(sensors[i] - sensors[i-1])
dist.sort(reverse=True)

for _ in range(K-1):
    if dist:
        dist.pop(0)

print(sum(dist))