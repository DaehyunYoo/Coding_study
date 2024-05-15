# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
    
#     for i in range (0, len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
        
#     return participant[-1]

from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]