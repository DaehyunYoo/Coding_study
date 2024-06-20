# 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
            
        else:
            if len(stack) == 0:
                return False
            
            else:
                stack.pop()
                
    if len(stack) != 0:
        return False
    
    
    return True