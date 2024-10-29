# 소수 찾기

from itertools import permutations

def solution(numbers):
    answer = []
    #string을 한 글자식 list로 담으려면 list(string)
    numbers= list(numbers)

    #순열을 사용한다.
    for i in range(len(numbers)):
        arr = list(permutations(numbers, i+1)) #순열로 변환 (튜플)
        arr = list(map(lambda x: int(''.join(list(x))) ,arr))

        for number in arr:
            isAnswer = True
            if number >1 and number not in answer:
                for i in range(2, number):
                    
                    if number % i == 0:
                        isAnswer = False
                        break
                if isAnswer == True:
                    answer.append(number)


    return len(list(set(answer)))