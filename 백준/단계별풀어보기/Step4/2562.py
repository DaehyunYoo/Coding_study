# 한 줄에 하나 입력으로 9줄 입력
X = [int(input()) for i in range(9)]

# X의 최댓값, 몇번째 줄인지 출력
print(max(X), X.index(max(X))+1, sep='\n')
