import itertools

def solution(word):
    alphabet = list("AEIOU")

    a_list = []
    for i in range(5):
        for k in list(itertools.product(alphabet, repeat=i + 1)):
            a_list.append("".join(k))
    a_list.sort()
    return a_list.index(word) + 1