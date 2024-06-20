# 영어 끝말잇기
# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    lst = [words[0]]
    for i in range(1, len(words)):
        if words[i][0] == words[i-1][-1] and words[i] not in lst:
            lst.append(words[i])
        else:
            return [i%n+1, i//n+1]
    
    return [0,0]