n, m, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
k -= 1

# 블럭이 놓일 위치를 찾는다
target_row = -1
for row in range(n):
    # 현재 행의 k부터 k+m까지의 공간이 모두 비어있는지 직접 확인
    block_present = False
    for col in range(k, k + m):
        if graph[row][col] == 1:
            block_present = True
            break
    
    if block_present:
        # 블럭이 있는 부분을 만났으므로 이전 행에 블럭을 놓는다
        target_row = row - 1
        break
else:
    # 만약 끝까지 비어있다면 마지막 행에 블럭을 놓는다
    target_row = n - 1

# 블럭이 내려오는 과정에서 지나간 부분을 다시 0으로 처리
for row in range(target_row + 1):
    if row != target_row:
        graph[row][k:k+m] = [0] * m
    else:
        # 마지막으로 도달한 곳에 블럭을 놓는다
        graph[row][k:k+m] = [1] * m

# 결과 출력
for i in graph:
    print(*i)
