# players = [[4], [8]]
players = [[8], [2]]

dice = 0
dice_throw_count = 0

winning_player = None
while winning_player is None:
    for player in range(2):
        dicethrows = []
        for dicethrow in range(1, 4):
            dice += 1
            dicethrows.append(dice)
            dice_throw_count += 1

        score = (players[player][-1] + sum(dicethrows)) % 10
        if score == 0:
            score = 10

        players[player].append(score)

        if sum(players[player][1:]) >= 1000:
            winning_player = player
            break

losing_player = 1 if winning_player == 0 else 0
losing_player_score = sum(players[losing_player][1:])

print(losing_player_score * dice_throw_count)
