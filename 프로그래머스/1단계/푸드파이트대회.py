def solution(food):
    player = '' 
    for i in range(1, len(food)):
        player += str(i) * (food[i]//2)
    return player + '0' + player[::-1]