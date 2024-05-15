def solution(dartResult):
    result = []
    score = 0 
    dartResult = dartResult.replace("10", "z")
    
    for n in dartResult:
        if n.isnumeric():
            score += int(n)
            continue
            
        elif n == 'z': 
            score += 10
            continue
            
        elif n == 'S':
            result.append(score)
            
        elif n == 'D':
            result.append(score ** 2)
            
        elif n == 'T':
            result.append(score ** 3)
            
        elif n == '*': 
            if len(result) > 1:
                result[-1] *= 2  
                result[-2] *= 2  
            else:
                result[-1] *= 2
                
        elif n == '#': 
            result[-1] *= -1
            
        score = 0 
        
    return sum(result)