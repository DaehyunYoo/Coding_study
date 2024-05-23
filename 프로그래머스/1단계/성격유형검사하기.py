def solution(survey, choices):
    answer = ''
    tp = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    score = {1: -3, 2: -2, 3: -1, 4: 0, 5: 1, 6: 2, 7: 3}
    
    for i in range(len(survey)):
        if score[choices[i]] > 0:
            tp[survey[i][1]] += score[choices[i]]
        elif score[choices[i]] < 0:
            tp[survey[i][0]] += abs(score[choices[i]])
        else:
            continue
    
    
    if tp['R'] >= tp['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if tp['C'] >= tp['F']:
        answer += 'C'
    else:
        answer += 'F'
    
    if tp['J'] >= tp['M']:
        answer += 'J'
    else:
        answer += 'M'
    
    if tp['A'] >= tp['N']:
        answer += 'A'
    else:
        answer += 'N'
            
    return answer