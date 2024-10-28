def solution(board, moves):
    answer = 0
    result = []
    n = len(board)
    
    for i in moves:
        for j in range(n):
            if board[j][i-1] != 0:
                result.append(board[j][i-1])
                board[j][i-1] = 0
                break
        
        if len(result) > 1 and result[-1] == result[-2]:
            result.pop()
            result.pop()
            answer += 2
    
    
    return answer
