# 빈 배열에 추가, 삭제하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181860

def solution(arr, flag):
    answer = []
    for idx, val in enumerate(flag):
        if val == True:
            for _ in range(arr[idx]*2):
                answer.append(arr[idx])
        else:
            for _ in range(arr[idx]):
                answer.pop()
    return answer