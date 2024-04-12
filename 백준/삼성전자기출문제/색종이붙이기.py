# 색종이 붙이기
# https://www.acmicpc.net/problem/17136

## DFS 풀이

from collections import deque

graph = [list(map(int, input().split())) for _ in range(10)]  # 10x10 그래프 입력

visited = [[False] * 10 for _ in range(10)]  # 방문 여부 체크 배열, 여기서는 사용되지 않음

papers = [0, 5, 5, 5, 5, 5]  # 사용 가능한 색종이 수(1x1부터 5x5까지)
result = set()  # DFS 실행 결과를 저장하는 집합

# 색종이 최대 길이 구하는 함수
def find_length(y, x):
    length = 1  # 시작 길이는 1
    for l in range(2, min(10 - y, 10 - x, 5) + 1):  # 2부터 (x, y로부터의 최소 거리, 5)까지 반복
        for i in range(y, y+l):
            for j in range(x, x+l):
                if graph[i][j] == 0:  # 0을 만나면 현재 길이 반환
                    return length
        length += 1  # 가능한 길이 증가
    return length

# 색종이 덮는 함수
def cover(y, x, length):
    for i in range(y, y + length):
        for j in range(x, x + length):
            graph[i][j] = 0  # 해당 영역을 0으로 변경
            
# 색종이 지우는 함수
def uncover(y, x, length):
    for i in range(y, y + length):
        for j in range(x, x + length):
            graph[i][j] = 1  # 해당 영역을 1로 복구

# DFS 함수
def DFS(cnt):
    for i in range(0, 10):
        for j in range(0, 10):
            if graph[i][j] != 0:  # 1을 만나면
                length = find_length(i, j)  # 최대 길이 계산
                for l in range(length, 0, -1):  # 최대 길이부터 1까지 반복
                    if papers[l]:  # 해당 크기의 색종이가 남아있다면
                        cover(i, j, l)  # 색종이로 덮기
                        papers[l] -= 1  # 사용한 색종이 감소
                        result.add(DFS(cnt + 1))  # DFS 재귀 호출
                        uncover(i, j, l)  # 색종이 제거
                        papers[l] += 1  # 사용했던 색종이 복구
                if result:  # 결과가 있다면 최소값 반환
                    return min(result)
                else:  # 결과가 없다면 -1 반환
                    return -1
    return cnt  # 모든 1을 덮었다면 현재까지 사용한 색종이 수 반환

result.add(DFS(0))
if -1 in result:
    result.remove(-1)
    
print(min(result) if result else -1)  # 결과 출력
