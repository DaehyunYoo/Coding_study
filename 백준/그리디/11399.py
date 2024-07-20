# ATM
# 11399

N = int(input())
P = list(map(int, input().split()))

P = sorted(P)
sum = 0
waiting = [0] * N
waiting[0] = P[0]

for i in range(1, N):
    waiting[i] = waiting[i - 1] + P[i]