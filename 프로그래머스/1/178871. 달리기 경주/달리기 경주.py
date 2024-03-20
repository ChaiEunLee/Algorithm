def solution(players, callings):
    calldict = {x : 0 for x in callings}
    playdict = {player : i for i,player in enumerate(players)}
    #print(playdict)
    for call in callings:
        idx = playdict[call]
        playdict[call] -= 1
        playdict[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players