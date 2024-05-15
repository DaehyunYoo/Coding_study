def solution(ingredient):
    answer = 0
    ham = []
    for i in ingredient:
        ham.append(i)
        if ham[-4:] == [1,2,3,1]:
            del ham[-4:]
            answer += 1
    return answer