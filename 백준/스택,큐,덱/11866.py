# 요세푸스 문제
# 11866

from collections import deque

N, K = map(int, input().split())

queue = deque()
result = []

for i in range(1, N+1):
    queue.append(i)

while len(queue) > 0:
    for j in range(1, K):
        queue.append(queue.popleft()) # 1, 2, ..., K-1까지는 popleft()로 뽑아서 뒤로 넘기기
    result.append(str(queue.popleft())) # K번째 값은 popleft()로 결과 창으로 추출

# print("<", ", ".join(result), ">")
print("<{}>".format(', '.join(result)))