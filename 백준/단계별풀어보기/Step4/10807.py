# 정수 개수가 주어짐
x = int(input())

# N개의 정수가 공백으로 주어짐
y = list(map(int, input().split()))    

# y에서 찾으려는 정수가 주어짐
v = int(input())

print(y.count(v))