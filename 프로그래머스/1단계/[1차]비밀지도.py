def solution(n, arr1, arr2):
    answer = []
    arr1_num, arr2_num = [], []
    for i in arr1:
        if len(bin(i)[2:]) != n:
            arr1_num.append('0' * (n - len(bin(i)[2:])) + bin(i)[2:])
        else:
            arr1_num.append(bin(i)[2:])
        
    
    for i in arr2:
        if len(bin(i)[2:]) != n:
            arr2_num.append('0' * (n - len(bin(i)[2:])) + bin(i)[2:])
        else:
            arr2_num.append(bin(i)[2:])
    
    for i in range(n):
        word = ''
        for j in range(n):
            if arr1_num[i][j] == '1' or arr2_num[i][j] == '1':
                word += '#'
            else:
                word += ' '
        answer.append(word)
    return answer

    