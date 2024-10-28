# 외계 행성의 나이
# https://school.programmers.co.kr/learn/courses/30/lessons/120834

def solution(age):
    age = str(age)
    age = age.replace("0", "a")
    age = age.replace("1", "b")
    age = age.replace("2", "c")
    age = age.replace("3", "d")
    age = age.replace("4", "e")
    age = age.replace("5", "f")
    age = age.replace("6", "g")
    age = age.replace("7", "h")
    age = age.replace("8", "i")
    age = age.replace("9", "j")
    return age

def solution(age):
    answer = ''
    for i in str(age):
        answer += chr(int(i) + 97)
    return answer