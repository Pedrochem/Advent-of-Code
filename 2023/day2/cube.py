with open("input.txt") as f:

    lines = f.readlines()

    max_red = 12
    max_green = 13
    max_blue = 14
    games = []

    for l in lines:

        game_id = int(l.split(":")[0].replace('Game ','') )
        possible = True

        while (' blue' in l):
            blue = int(l.split(' blue')[0].split(' ')[-1])
            l = l.replace(' blue','X',1)
            if blue > max_blue:
                possible = False

        while (' green' in l):
            green = int(l.split(' green')[0].split(' ')[-1])
            l = l.replace(' green','X',1)
            if green > max_green:
                possible = False

        while (' red' in l):
            red = int(l.split(' red')[0].split(' ')[-1])
            l = l.replace(' red','X',1)
            if red > max_red:
                possible = False
        
        if possible: games.append(game_id)
    
    print(sum(games))