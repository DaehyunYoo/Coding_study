# 거스름돈
# 5585

import sys
input = sys.stdin.readline

N = int(input())
exchange = 1000 - N

moneys = [500, 100, 50, 10, 5, 1]
result = 0

for i in moneys:
    if exchange == 0:
        break
    
    result += exchange // i
    exchange %= i
    
print(result)