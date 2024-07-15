# 블랙잭
# 2798

N, M = map(int, input().split())
lst = list(map(int, input().split()))
result = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            three =  lst[i] + lst[j] + lst[k]
            if three > M:
                continue
            else:
                result.append(three)
print(max(result))