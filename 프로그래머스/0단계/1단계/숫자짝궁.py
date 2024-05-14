from collections import Counter

def solution(X, Y):
    answer = ''
    x = Counter(X)
    y = Counter(Y)
    
    for i in range(10):
        answer += str(i) * (min(x[str(i)], y[str(i)]))
    
    if answer == '':
        return '-1'
    
    answer = ''.join(sorted(answer, reverse=True))
    if len(answer) == answer.count('0'):
        return '0'
    else:
        return answer