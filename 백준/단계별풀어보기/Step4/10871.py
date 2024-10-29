# N, x가 주어짐
N, x = map(int, input().split())

# 수열 A를 이루는 정수 N개가 주어짐
A = list(map(int, input().split()))

# x보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력
for i in range(N):
    if A[i] < x:
        print(A[i], end=' ')
