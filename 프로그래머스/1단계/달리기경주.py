# def solution(players, callings):

#     for i in callings:
#         n = players.index(i)
#         players[n], players[n-1] = players[n-1], players[n]
#     return players

def solution(players, callings):
    lst = {player: i for i, player in enumerate(players)} 
    
    for j in callings:
        idx = lst[j] 
        lst[j] -= 1 
        lst[players[idx-1]] += 1 
        players[idx-1], players[idx] = players[idx], players[idx-1] 
        
    return players