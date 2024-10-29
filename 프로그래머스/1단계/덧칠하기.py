def solution(n, m, section):
    answer = 1
    paint = section[0] # 덧칠 시작점
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            print(section[i], paint)
            answer += 1
            paint = section[i]
    return answer