def solution(s, skip, index):
    answer = ''
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    for i in skip:
        alpha = alpha.replace(i, "")
    
    for i in s:
        new = alpha[(alpha.index(i) + index) % len(alpha)]
        answer += new

    
    return answer