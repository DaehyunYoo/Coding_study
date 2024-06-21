# 괄호
# 9012

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    stack = []
    paren = input()
    for i in paren:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')
    