def solution(k, score):
    lst, answer = [],[]
    
    for i in score:
        lst.append(i)
        lst = sorted(lst, reverse=True)
        
        if len(lst) > k:
            lst.pop()

        answer.append(lst[-1])
    return answer