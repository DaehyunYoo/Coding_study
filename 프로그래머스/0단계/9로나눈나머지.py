# 9로 나눈 나머지
# https://school.programmers.co.kr/learn/courses/30/lessons/181914

def solution(number):
    result = 0
    for num in str(number):
        result += int(num)
    answer = result % 9
    return answer

def solution(number):
    return sum(list(map(int, number))) % 9