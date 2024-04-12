# 괄호 추가하기
# https://www.acmicpc.net/problem/16637

from collections import deque

def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

# BFS 함수 정의
def bfs(expression):
    max_value = float('-inf')  # 최댓값 초기화
    queue = deque([(int(expression[0]), 0)])  # 초기 상태와 인덱스를 큐에 저장
    
    while queue:  # 큐가 빌 때까지 반복
        current_value, index = queue.popleft()
        
        # 모든 연산자를 고려했을 때, 최댓값 업데이트
        if index >= len(expression) - 1:
            max_value = max(max_value, current_value)
            continue
        
        # 현재 위치에서 괄호를 추가하지 않고 계산을 진행하는 경우
        op = expression[index + 1]
        next_value = int(expression[index + 2])
        queue.append((calculate(current_value, op, next_value), index + 2))
        
        # 현재 위치에서 괄호를 추가하여 계산을 진행하는 경우
        if index + 2 < len(expression) - 1:
            op2 = expression[index + 3]
            next_value2 = int(expression[index + 4])
            # 괄호 안의 연산 먼저 수행
            bracket_result = calculate(next_value, op2, next_value2)
            # 그 결과를 현재까지의 결과와 연산
            queue.append((calculate(current_value, op, bracket_result), index + 4))
    
    return max_value

# 입력
N = int(input())  # 수식의 길이
expression = input().strip()  # 수식

# BFS를 이용한 결과의 최댓값 계산
max_result = bfs(expression)

# 결과 출력
print(max_result)
