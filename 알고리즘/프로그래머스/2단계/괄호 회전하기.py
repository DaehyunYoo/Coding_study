# 괄호 회전하기
# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer = 0
    s = list(s)
    
    for _ in range(len(s)):
        stack = []
        for i in range(len(s)):
            if len(stack) > 0:
                if stack[-1] == '[' and s[i] == ']':
                    stack.pop()
                elif stack[-1] == '{' and s[i] == '}':
                    stack.pop()
                elif stack[-1] == '(' and s[i] == ')':
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                # stack에 아무것도 없으면 그냥 추가
                stack.append(s[i])
            print(stack)
        s.append(s.pop(0)) # 왼쪽으로 회전
        
        # stack에 남아있는게 없으면 올바른 괄호 문자열이라는 의미이므로 +1
        if len(stack) == 0:
            answer += 1

    
    return answer