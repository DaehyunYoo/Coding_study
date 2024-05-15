def solution(s):
    answer = 0  
    is_x, not_x = 0, 0  
    for i in range(len(s)):
        if is_x == not_x:  
            answer += 1
            x = s[i]
            is_x, not_x = 0, 0
            
        if s[i] == x:
            is_x += 1
        else:
            not_x += 1
            
    return answer