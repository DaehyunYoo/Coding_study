# 백준 2847
# 게임을 만든 동준이

N = int(input())
score = []
for _ in range(N):
    score.append(int(input()))

count = 0
# 뒤에서부터 앞으로 검사
for i in range(N-2, -1, -1):
    # 현재 점수가 다음 레벨 점수보다 크거나 같으면
    if score[i] >= score[i+1]:
        # 감소시켜야 하는 양 계산
        diff = score[i] - score[i+1] + 1
        count += diff
        score[i] -= diff

print(count)