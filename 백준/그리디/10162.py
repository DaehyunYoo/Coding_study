# 전자레인지

T = int(input())

A, B, C = 300, 60, 10

result = [0, 0, 0]

while T >= 10:
    if T >= A:
        result[0] += T // A
        T %= A
    elif T < A and T >= B:
        result[1] += T // B
        T %= B
    elif T < B and T >= C:
        result[2] += T // C
        T %= C

if T != 0:
    print(-1)
else:
    print(f'{result[0]} {result[1]} {result[2]}')
    