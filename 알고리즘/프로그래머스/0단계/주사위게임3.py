# 주사위 게임 3 - 파이썬
# https://school.programmers.co.kr/learn/courses/30/lessons/181916


def solution(a, b, c, d):
    nums = [a, b, c, d]
    counts = []
    for i in nums:
        counts.append(nums.count(i))

    if max(counts) == 4:
        score = a * 1111

    elif max(counts) == 3:
        p = nums[counts.index(3)]
        q = nums[counts.index(1)]
        score =  (10 * p + q) ** 2

    elif max(counts) == 2:
        if min(counts) == 2:
            score = (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        else:
            p = nums[counts.index(2)]
            score =  (a * b * c * d) / p**2
    else:
        score = min(nums)

    return score