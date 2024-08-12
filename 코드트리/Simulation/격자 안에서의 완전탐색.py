
N = int(input())

graph = [[] for _ in range(N)]

for i in range(N):
    a = list(map(int, input().split()))
    graph[i] = a

max_coin = 0

for i in range(N-2):
    for j in range(N-2):
        coin = 0
        for x in range(3):
            for y in range(3):
                coin += graph[i+x][j+y]
        max_coin = max(max_coin, coin)

print(max_coin)