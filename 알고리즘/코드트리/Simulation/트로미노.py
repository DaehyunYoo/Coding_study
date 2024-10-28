n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input()))

max_sum = 0

# ㄴ모양 블럭
for i in range(1, n):
    for j in range(m-1):
        if graph[i][j] + graph[i-1][j] + graph[i][j+1] > max_sum:
            max_sum = graph[i][j] + graph[i-1][j] + graph[i][j+1]
        else:
            continue

# ㄱ모양 
for i in range(n-1):
    for j in range(1, m):
        if graph[i][j] + graph[i][j-1] + graph[i+1][j] > max_sum:
            max_sum = graph[i][j] + graph[i][j-1] + graph[i+1][j]
        else:
            continue

for i in range(n-1):
    for j in range(m-1):
        if graph[i][j] + graph[i][j+1] + graph[i+1][j] > max_sum:
            max_sum = graph[i][j] + graph[i][j+1] + graph[i+1][j]
        else:
            continue

for i in range(1, n):
    for j in range(1, m):
        if graph[i][j] + graph[i-1][j] + graph[i][j-1] > max_sum:
            max_sum = graph[i][j] + graph[i-1][j] + graph[i][j-1]
        else:
            continue

# 1자 모양
for i in range(1, n-1):
    for j in range(m):
        if graph[i][j] + graph[i-1][j] + graph[i+1][j] > max_sum:
            max_sum = graph[i][j] + graph[i-1][j] + graph[i+1][j]
        else:
            continue

for i in range(n):
    for j in range(1, m-1):
        if graph[i][j] + graph[i][j-1] + graph[i][j+1] > max_sum:
            max_sum = graph[i][j] + graph[i][j-1] + graph[i][j+1]
        else:
            continue

print(max_sum)

