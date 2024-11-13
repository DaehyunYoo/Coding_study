# 백준 27961
# 고양이는 많을수록 좋다

import sys
input = sys.stdin.readline  

N = int(input())  # 목표 고양이 수
cat = 1          # 현재 고양이 수 (첫 번째 고양이 생성 가정)
count = 0        # 행동 횟수

# 특수 케이스 처리
if N == 0:      # 고양이가 필요 없는 경우
    print(0)
elif N == 1:    # 고양이 1마리만 필요한 경우
    print(1)
else:
    while cat != N:  # 현재 고양이 수가 목표와 다른 동안 반복
        # 남은 필요한 고양이 수(N - cat)가 현재 고양이 수(cat) 이하인 경우
        if cat >= N - cat:
            cat += N - cat  # 필요한 만큼만 추가
            count += 1
        # 현재 고양이 수를 모두 복제해도 괜찮은 경우
        else:
            cat += cat      # 현재 수만큼 복제
            count += 1
    print(count + 1)  # 첫 번째 고양이 생성 횟수를 더해줌