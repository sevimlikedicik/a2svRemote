def predictPartyVictory(senate: str) -> str:
    bans = {
        'D': {'opp': 'R', 'ban': 0},
        'R': {'opp': 'D', 'ban': 0}
    }
    # kind of a poetic code if you ask me
    senate = [c for c in senate]

    one_party_rule = False
    while not one_party_rule:
        for i in range(0, len(senate)):
            if senate[i] == 'X':
                continue
            if bans[bans[senate[i]]['opp']]['ban'] > 0:
                bans[bans[senate[i]]['opp']]['ban'] -= 1
                senate[i] = 'X'
            else:
                bans[senate[i]]['ban'] += 1

        one_party_rule = len(set(senate)) <= 2

    for senator in senate:
        if senator == 'X':
            continue
        if senator == 'D':
            return 'Dire'
        return 'Radiant'
