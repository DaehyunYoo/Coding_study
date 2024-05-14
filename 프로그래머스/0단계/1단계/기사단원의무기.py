def solution(number, limit, power):
    answer = 0
    lst = []
    
    for n in range(1, number+1):
        count = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if i == (n // i):
                    count += 1
                else:
                    count += 2
        lst.append(count)
    
    for k in lst:
        if k > limit:
            answer += power
        else:
            answer += k
    return answer
