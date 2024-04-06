# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

C = int(input())

for _ in range(C):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:])/scores[0]
    cnt = 0

    for i in scores[1:]:
        if i > avg:
            cnt += 1
    per = (cnt/scores[0])*100
    
    print(f'{per:.3f}%' + '%')