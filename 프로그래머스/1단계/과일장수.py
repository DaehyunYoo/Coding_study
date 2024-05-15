def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    boxes = []
    for i in range(0, len(score), m):    
        boxes.append(score[i:i+m])
    
    for i in range(len(boxes)):
        if len(boxes[i]) == m:
            answer += (min(boxes[i]) * m)
    return answer
