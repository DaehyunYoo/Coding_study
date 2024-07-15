# 기능개발

from collections import Counter

def solution(progresses, speeds):
    days = []
    for i in range(len(speeds)):
        if (100 - progresses[i]) % speeds[i] != 0:
            days.append((100 - progresses[i]) // speeds[i] + 1) 
        else:
            days.append((100 - progresses[i]) // speeds[i])
    
    result = [days[0]]
    for k in range(1, len(days)):
        if result[-1] < days[k]:
            result.append(days[k])
        else:
            result.append(result[-1])
    
    count = Counter(result)
    answer = list(count.values())
            
    
    return answer

from collections import Counter

def solution(progresses, speeds):
    days = []
    for i in range(len(speeds)):
        if (100 - progresses[i]) % speeds[i] != 0:
            days.append((100 - progresses[i]) // speeds[i] + 1) 
        else:
            days.append((100 - progresses[i]) // speeds[i])
    
    result = [days[0]]
    for k in range(1, len(days)):
        if result[-1] < days[k]:
            result.append(days[k])
        else:
            result.append(result[-1])
    
    count = Counter(result)
    answer = list(count.values())
            
    
    return answer