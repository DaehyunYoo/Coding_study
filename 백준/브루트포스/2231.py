# 분해합
# 2231

N = int(input())

for i in range(N):
    digit_sum = i + sum(map(int, str(i)))
    
    if digit_sum == N:
        print(i)
        break
else:
    print(0)