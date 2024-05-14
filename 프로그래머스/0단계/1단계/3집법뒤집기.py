def solution(n):
    answer = ''
    
    while n >= 1:
        rest = n % 3
        n = n // 3
        answer += str(rest)
        
    return int(answer, 3)

# def solution(n):
#     answer = ''

#     while n >= 0:			
#         n, re = divmod(n,3)	
#         answer += str(re)
#     return int(answer, 3)