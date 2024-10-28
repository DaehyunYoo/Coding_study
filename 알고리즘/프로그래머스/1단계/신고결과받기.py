# 신고 결과 받기
# 

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    rept = {x: 0 for x in id_list}
    
    # 중복 신고 제거
    for i in set(report):
        a, b = i.split(' ')
        rept[b] += 1
    
    for j in set(report):
        a, b = j.split(' ')
        if rept[b] >= k:
            answer[id_list.index(a)] += 1
    
    return answer