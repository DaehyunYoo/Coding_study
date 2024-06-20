# 최댓값과 최솟값
# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    
    dic = {int(x) for x in s.split(' ')}
    return str(min(dic)) + " " + str(max(dic))