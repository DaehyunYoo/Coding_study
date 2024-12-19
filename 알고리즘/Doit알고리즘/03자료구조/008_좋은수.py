# '좋은 수' 구하기
# 백준 1253

N = int(input())
nums = list(map(int, input().split()))

nums.sort()
count = 0

for k in range(len(nums)):
    target = nums[k]
    i = 0
    j = N - 1
    
    while i < j:
        if nums[i] + nums[j] == target:
            if i != k and j != k:
                count += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1

print(count)