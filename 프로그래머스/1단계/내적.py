def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

def solution(a, b):
    answer = 0
    for a, b in zip(a, b):
        answer += a * b
    return answer