def solution(s):
    answer = []
    dic = {}
    
    for idx, word in enumerate(s):
        if word not in dic:
            answer.append(-1)
            dic[word] = idx
        else:
            answer.append(idx - dic[word])
            dic[word] = idx
    return answer