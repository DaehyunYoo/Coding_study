# 무작위로 K개의 개수 뽑기
# https://school.programmers.co.kr/learn/courses/30/lessons/181858

def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if arr[i] in answer:
            continue
        else:
            answer.append(arr[i])

    if len(answer) < k:
        for _ in range(k - len(answer)):
            answer.append(-1)
    elif len(answer) > k:
        for _ in range(len(answer) - k):
            answer.pop()
        else:
            answer = answer


    return answer

def solution(arr, k):
    ret = []
    for i in arr:
        if i not in ret:
            ret.append(i)
        if len(ret) == k:
            break

    return ret + [-1] * (k - len(ret))