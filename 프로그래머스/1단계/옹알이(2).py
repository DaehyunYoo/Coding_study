def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        for j in words:
            if j in i and j*2 not in i:
                i = i.replace(j, " ")
        if i.isspace():
            answer += 1
    return answer
