# 신기한 소수 찾기
# 백준 2023

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())

# isPrime: num이 소수인지 판별
def isPrime(num):
    for i in range(2, int(num / 2 + 1)): # 절반만으로 소수 판별이 가능. 그 이상은 낭비
        if num % i == 0:
            return False
    return True

def DFS(number):
    if len(str(number)) == N:
        print(number)
    
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if isPrime(number * 10 + i): # 현재 숫자 number 뒤에 i를 더했을 때 소수인지 확인
                DFS(number * 10 + i)
            
DFS(2)
DFS(3)
DFS(5)
DFS(7)