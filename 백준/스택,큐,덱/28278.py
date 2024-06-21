# 28278
# 스택 2
import sys
input = sys.stdin.readline

N = int(input())

stack = []
result = []


for i in range(N):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        stack.append(lst[1])
    elif lst[0] == 2:
        if len(stack) != 0:
            result.append(stack.pop())
        else:
            result.append(-1)
    elif lst[0] == 3:
        result.append(len(stack))
    elif lst[0] == 4:
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    else:
        if len(stack) != 0:
            result.append(stack[-1])
        else:
            result.append(-1)

for j in range(len(result)):
    print(result[j])