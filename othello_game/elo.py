AI_ELO_BY_DEPTH = {1:700, 2:900, 3:1100, 4:1300, 5:1500, 6:1700, 7:1900}
K_FACTOR = 32
def expected_score(p,o): return 1/(1+10**((o-p)/400))
def new_elo(player_elo, opponent_elo, result):
    score={'win':1.0,'loss':0.0,'draw':0.5}[result]
    change=round(K_FACTOR*(score-expected_score(player_elo,opponent_elo)))
    return max(100,player_elo+change), change
