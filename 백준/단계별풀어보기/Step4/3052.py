# 한 줄에 두개씩 10줄 입력
x = [int(input()) for i in range(10)]

# 42로 나눴을때 나머지
y = [i%42 for i in x]

# set으로 중복 제거
y = set(y)

print(len(y))