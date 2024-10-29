# 균형잡힌 세상
# 4949

while True :
    word = input()
    stack = []

    if word == "." :
        break

    for i in word :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() 
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if not stack:
        print('yes')
    else :
        print('no')