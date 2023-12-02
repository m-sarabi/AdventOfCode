limit = {'green': 13, 'blue': 14, 'red': 12}

with open("input.txt", 'r') as file:
    games = file.readlines()
result = 0
for game_id, game in enumerate(games):
    bad = False
    sub_games = game.split(':')[1].split('; ')
    for sub in sub_games:
        sub_game_balls = sub.strip().split(', ')
        for i in sub_game_balls:
            if limit[i.split()[1]] < int(i.split()[0]):
                bad = True
                break
        if bad:
            break
    if not bad:
        result += (game_id + 1)
print(result)

# 2169
