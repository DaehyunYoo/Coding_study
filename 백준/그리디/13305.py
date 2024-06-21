# 주유소
# 13305

import sys
input = sys.stdin.readline

N = int(input())

road = list(map(int, input().split()))

price = list(map(int, input().split()))

now_price = price[0]
cost = 0

for i in range(N-1):
    if price[i] < now_price:
        now_price = price[i]
    
    cost += now_price * road[i]

print(cost)