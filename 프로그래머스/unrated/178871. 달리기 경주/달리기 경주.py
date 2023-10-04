def solution(players, callings):
    player_dict = {}
    
    for idx, player in enumerate(players):
        player_dict[player] = idx
    
    for c in callings:
        idx = player_dict[c]
        player_dict[c] -= 1
        player_dict[players[idx - 1]] += 1
        
        players[idx-1], players[idx] = players[idx], players[idx-1]
    
    return players