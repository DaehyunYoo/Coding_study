# 도키도키 간식드리미
# 12789

import sys
input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))

stack = []
turn = 1 # 지금 간식 받는 순서

for i in num:
    stack.append(i)
    
    while stack and stack[-1] == turn:
        stack.pop()
        turn += 1

if stack:
    print("Sad")
else:
    print("Nice")