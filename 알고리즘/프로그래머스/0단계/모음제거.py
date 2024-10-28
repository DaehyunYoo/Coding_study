# 모음 제거
# https://school.programmers.co.kr/learn/courses/30/lessons/120849

def solution(my_string):
    answer = ''
    delete = ['a','e','i','o','u']
    for i in my_string:
        if i not in delete:
            answer += i
    return answer


def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string

def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])