def solution(x):
    num = 0
    
    for i in range(len(str(x))):
        num += int(str(x)[i])
    
    if x % num == 0:
        return True
    else:
        return False
    