# N, M = map(int(input().split()))

# basket = [0 for i in range(N)]

# # 각 줄에 3개씩 M개줄 입력받기
# for _ in range(M):
#     i, j, k = map(int, input().split())
#     for n in range(i, j+1):
#         basket[n] = k 

# for i in range(1, N+1):
#     print(basket[i], end = ' ') 

N,M =map(int, input().split())
l_s=[0 for i in range(N)]

for a in range(M):
    i,j,k=map(int, input().split())
    for b in range(i,j+1):
        l_s[b-1]=k

for i in range(N):
    print(l_s[i],end=" ")