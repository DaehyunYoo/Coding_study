# DNA 비밀번호 구하기 
# 백준 12891

# 문자열 길이(S)와 부분문자열 길이(P) 입력
S, P = map(int, input().split())
# DNA 문자열 입력
DNA = input().rstrip()  # 개행문자 제거
# 각 문자의 최소 개수 입력
min_cnt = list(map(int, input().split()))  # [A, C, G, T]

# 현재 윈도우의 문자 개수를 저장할 딕셔너리
check = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
result = 0

# 초기 윈도우에 대한 문자 개수 계산
for i in range(P):
    check[DNA[i]] += 1

# 초기 윈도우가 조건을 만족하는지 확인
if (check['A'] >= min_cnt[0] and 
    check['C'] >= min_cnt[1] and 
    check['G'] >= min_cnt[2] and 
    check['T'] >= min_cnt[3]):
    result += 1

# 슬라이딩 윈도우 이동
for i in range(P, S):
    # 이전 윈도우의 첫 문자 제거
    check[DNA[i-P]] -= 1
    # 새로운 문자 추가
    check[DNA[i]] += 1
    
    # 현재 윈도우가 조건을 만족하는지 확인
    if (check['A'] >= min_cnt[0] and 
        check['C'] >= min_cnt[1] and 
        check['G'] >= min_cnt[2] and 
        check['T'] >= min_cnt[3]):
        result += 1

print(result)