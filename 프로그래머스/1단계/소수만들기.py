from itertools import combinations

def solution(nums):
    answer = 0
    for combo in combinations(nums, 3):
        n = sum(combo)
        for i in range(2, int(n**(0.5))+1):
            if n % i == 0:
                ab = False
                break
            else:
                ab = True
        if ab is True:
            answer += 1
    return answer
