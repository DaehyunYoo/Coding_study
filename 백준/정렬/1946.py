# # 신입 사원
# # 1946
# import sys
# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     candidates = []

#     for _ in range(N):
#         s, m = map(int, input().split())
#         candidates.append((s, m))
    
#     candidates.sort()

#     top = 1e9
#     count = 0

#     for i in range(N):
#         if candidates[i][1] < top:
#             count += 1
#             top = candidates[i][1]
    
#     print(count)
        
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    candidates = []
    for _ in range(N):
        a, b = map(int, input().split())
        candidates.append((a, b))
    candidates.sort()
    
    top = 1e9
    count = 0
    
    for i in range(N):
        if candidates[i][1] < top:
            count += 1
            top = candidates[i][1]
    
    print(count)