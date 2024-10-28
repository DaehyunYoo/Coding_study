# 프로세스

from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(idx, value) for idx, value in enumerate(priorities)])

    while queue:
        item = queue.popleft()
        if queue and max(queue, key=lambda x: x[1])[1] > item[1]:
            queue.append(item)
        else:
            answer += 1
            if item[0] == location:
                break
    return answer

from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(idx, value) for idx, value in enumerate(priorities)])

    while queue:
        item = queue.popleft()
        # 큐에서 최대 우선순위를 찾는 부분
        if queue:  # 큐가 비어있지 않을 때만 최대값 비교
            max_priority = max([priority for idx, priority in queue])
            if max_priority > item[1]:
                queue.append(item)
            else:
                answer += 1
                if item[0] == location:
                    break
        else:  # 큐가 비어있다면 현재 아이템이 최고 우선순위
            answer += 1
            if item[0] == location:
                break

    return answer
