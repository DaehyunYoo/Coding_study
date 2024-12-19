# 연속된 자연수의 합 구하기
# 백준 2018

N = int(input())

count = 1 # N = end가 같은 경우는 이미 포함

start = 1
end = 1
sum = 1 # 초기 1부터 시작 

while end != N:
    if sum == N:
        count += 1
        end += 1
        sum += end
    elif sum > N:
        sum -= start
        start += 1
    else:
        end += 1
        sum += end

print(count)