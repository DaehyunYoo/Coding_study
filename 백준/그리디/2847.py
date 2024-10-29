# 게임을 만든 동준이
# 2847

N = int(input())
lst = []

for i in range(N):
    A = int(input())
    lst.append(A)

count = 0

for i in range(N-2, -1, -1):
    if lst[i] >= lst[i+1]:
        count += lst[i] - (lst[i+1] - 1)
        lst[i] = lst[i+1] - 1

print(count)