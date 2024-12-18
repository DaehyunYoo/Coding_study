# 숫자의 합 구하기
# 백준 11720

N = int(input())
nums = list(input())
result = 0
for i in nums:
    result += int(i)
    
print(result)