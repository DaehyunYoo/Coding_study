
n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

result = 0

for i in range(n):
    count = 1
    for j in range(1, n):
        if graph[i][j] == graph[i][j-1]:
            count += 1
            if count >= m:
                result += 1
                break
        else:
            count = 1
    else:
        if count >= m:
            result += 1

for j in range(n):
    count = 1
    for i in range(1, n):
        if graph[i][j] == graph[i-1][j]:
            count = 1
            if count >= m:
                result += 1
                break
        else:
            count = 1
    else:
        if count >= m:
            result += 1

print(result)