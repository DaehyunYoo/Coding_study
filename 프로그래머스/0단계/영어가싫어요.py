# 프로그래머스
# 영어가 싫어요
# https://school.programmers.co.kr/learn/courses/30/lessons/120894

def solution(numbers):
    words = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
             'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for i in words.keys():
        numbers = numbers.replace(i, words[i])

    return int(numbers)