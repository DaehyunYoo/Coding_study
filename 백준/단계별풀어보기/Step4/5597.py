# 한 줄에 두개씩 28줄 입력
x = [int(input()) for i in range(28)]

# 1~30까지의 수를 리스트로 만듦
y = [i for i in range(1,31)]

# 제출 안한 학생 출석번호 출력
# list y 에서 x를 빼고 남은 번호 출력
for i in range(30):
    if y[i] not in x:
        print(y[i])