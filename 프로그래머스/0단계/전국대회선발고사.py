# 전국 대회 선발 고사
# https://school.programmers.co.kr/learn/courses/30/lessons/181851

def solution(rank, attendance):
    result = []

    for idx, val in enumerate(rank):
        if attendance[idx] == True:
            result.append([rank[idx], idx]) # 등수 & 번호

    result.sort()

    a = result[0][1]
    b = result[1][1]
    c = result[2][1]

    return 10000 * a + 100 * b + c

def solution(rank, attendance):
    n = len(rank)
    answer =0
    r_a = []

    for i in range(n):
        if attendance[i]:
            r_a.append([rank[i], i])

    r_a.sort(key = lambda v : v[0])

    return 10000 * r_a[0][1] + 100 * r_a[1][1] + r_a[2][1]