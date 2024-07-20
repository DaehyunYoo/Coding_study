# 먹을 것인가 먹힐 것인가
# 7795

T = int(input())

for _ in range(T):
    N, M = list(map(int, input().split()))
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A = sorted(A)
    B = sorted(B)
    
    main = 0  # A 포인터
    sub = 0 # B 포인터
    count = 0
    
    while main < N:
        if sub == M:
            count += sub
            main += 1
        else:
            if A[main] > B[sub]:
                sub += 1
            else:
                count += sub
                main += 1
    print(count)
                