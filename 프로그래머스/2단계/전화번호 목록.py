# 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True


def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 0
    
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer