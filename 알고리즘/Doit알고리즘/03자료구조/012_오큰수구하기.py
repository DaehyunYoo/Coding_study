# 오큰수 구하기
# 백준 17298

N = int(input())
A = list(map(int, input().split()))

answer = [-1] * N
stack = [0] # 0번 인덱스

for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)