# 회사 문화 1
# 14267

n, m = map(int, input().split())
parent = list(map(int, input().split()))

for i in range(1, n):
    parent[i] -= 1

result = [0] * n

for _ in range(m):
    id, score = map(int, input().split())    
    result[id-1] += score

total_result = [0] * n
for i in range(1, n):
    total_result[i] = total_result[parent[i]] + result[i]

print(*total_result)