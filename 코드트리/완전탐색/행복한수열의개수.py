'''
1이상 100이하의 숫자로만 이루어져 있는 n * n 크기의 격자 정보가 주어집니다.

이때 행복한 수열이라는 것은 다음과 같이 정의됩니다.

행복한 수열 = 연속하여 m개 이상의 동일한 원소가 나오는 순간이 존재하는 수열
n * n 크기의 격자 정보가 주어졌을 때 각 행마다 봤을 때 나오는 n개의 수열과, 각 열마다 봤을 때 나올 수 있는 n개의 수열을 포함하여 총 2n개의 수열 중 행복한 수열의 개수를 세서 출력하는 프로그램을 작성해보세요.

예를 들어, 다음과 같은 경우라면, 첫 번째 행을 골랐을 경우와 첫 번째 열을 골랐을 경우에만 행복한 수열이 되므로, 총 행복한 수열의 수는 2개가 됩니다.



입력 형식
첫 번째 줄에는 격자의 크기를 나타내는 n과 연속해야 하는 숫자의 수를 나타내는 m이 공백을 사이에 두고 주어집니다.

두 번째 줄부터는 n개의 줄에 걸쳐 격자에 대한 정보가 주어집니다. 각 줄에는 각각의 행에 대한 정보가 주어지며, 이 정보는 1이상 100이하의 숫자가 각각 공백을 사이에 두고 주어집니다.

1 ≤ m ≤ n ≤ 100
출력 형식
2n개의 수열들 중 행복한 수열의 수를 출력해주세요.

입출력 예제
예제1
입력:

3 2
1 2 2
1 3 4
1 2 3
출력:

2
예제2
입력:

3 1
1 2 3
4 5 6
7 8 8
출력:

6
제한
시간 제한: 1000ms
메모리 제한: 80MB
'''

n, m = map(int, input().split())
graph = []

for i in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

result = 0

# 행 검사
for i in range(n):
    count = 1
    for j in range(1, n):
        if graph[i][j] == graph[i][j - 1]:
            count += 1
            if count >= m:
                result += 1
                break
        else:
            count = 1
    else:
        if count >= m:
            result += 1

# 열 검사
for j in range(n):
    count = 1
    for i in range(1, n):
        if graph[i][j] == graph[i - 1][j]:
            count += 1
            if count >= m:
                result += 1
                break
        else:
            count = 1
    else:
        if count >= m:
            result += 1

print(result)