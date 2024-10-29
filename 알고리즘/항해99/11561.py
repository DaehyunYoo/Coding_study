# # 징검다리
# # 밟을 수 있는 최대 징검다리 수 
# T = int(input())

# for _ in range(T):
#     N = int(input()) # 총 징검다리 수
    
#     # 해당 테스트 케이스의 징검다리를 건너는 최대 수
#     result = 0 
#     for i in range(1, N+1):
#         result += i
#         if result > N:
#             result -= i
#             break

#     print(result)
    
# 시간 초과 해결

T = int(input())

for _ in range(T):
    N = int(input())
    start = 0
    end = 10**9
    
    while start < end:
        mid = (start + end) // 2
        if mid * (mid + 1) // 2 <= N:
            start = mid + 1
        else:
            end = mid
    print(start - 1)