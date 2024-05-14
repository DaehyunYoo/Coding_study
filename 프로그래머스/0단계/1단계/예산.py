def solution(d, budget):
    answer = 0
    result = 0
    for i in sorted(d):
        result += i
        answer += 1
        if result > budget:
            return answer - 1
    return answer