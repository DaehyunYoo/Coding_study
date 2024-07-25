# 결혼식
# 5567

n = int(input())
m = int(input())

adj = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)
