
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

r, c = map(int, input().split())


bomb_length = graph[r-1][c-1] # 2

# 폭탄 영향 범위 처리
graph[r-1][c-1] = 0
for i in range(1, bomb_length):
    # 위로 범위 체크 후 0으로 변경
    if r-1-i >= 0:
        graph[r-1-i][c-1] = 0
    # 아래로 범위 체크 후 0으로 변경
    if r-1+i < n:
        graph[r-1+i][c-1] = 0
    # 왼쪽으로 범위 체크 후 0으로 변경
    if c-1-i >= 0:
        graph[r-1][c-1-i] = 0
    # 오른쪽으로 범위 체크 후 0으로 변경
    if c-1+i < n:
        graph[r-1][c-1+i] = 0


for col in range(n):
    # 열의 값을 아래로 압축
    temp = []  # 새로운 열을 저장할 빈 리스트 생성

    # 모든 행에 대해 반복
    for row in range(n):
        if graph[row][col] != 0:  # 현재 위치의 값이 0이 아니라면
            temp.append(graph[row][col])  # 그 값을 temp 리스트에 추가
    # 남은 공간을 0으로 채우기
    temp = [0] * (n - len(temp)) + temp
    
    # 재배치된 열을 다시 그래프에 반영
    for row in range(n):
        graph[row][col] = temp[row]

# print(graph)
for i in range(n):
    print(*graph[i])