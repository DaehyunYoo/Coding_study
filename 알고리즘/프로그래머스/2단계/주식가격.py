# 주식가격


from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        now_cost = queue.popleft()
        result = 0
        for i in queue:
            if now_cost <= i:
                result += 1
            else:
                result += 1
                break
            
        answer.append(result)
                
    return answer