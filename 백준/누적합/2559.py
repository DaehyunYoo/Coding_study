# 수열
# 2559

N, K = map(int, input().split())

temp = list(map(int, input().split()))

psum = [0]

for i in range(1, N):
    psum.append(psum[i-1] + temp[i])

temp_sum = [psum[i+K-1]]

for i in range(0, N - K + 1):
    if i == 0:
        sum = psum[i + K - 1]
    else:
        sum = psum[i + K - 1] - psum[i - 1]
    
    temp_sum.append(sum)
print(max(temp_sum))