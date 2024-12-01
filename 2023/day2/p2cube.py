with open("input.txt") as f:

    lines = f.readlines()


    powers = []

    for l in lines:
        max_red = 0
        max_green = 0 
        max_blue = 0
        game_id = int(l.split(":")[0].replace('Game ','') )
        possible = True

        while (' blue' in l):
            blue = int(l.split(' blue')[0].split(' ')[-1])
            l = l.replace(' blue','X',1)
            if blue > max_blue:
                max_blue = blue

        while (' green' in l):
            green = int(l.split(' green')[0].split(' ')[-1])
            l = l.replace(' green','X',1)
            if green > max_green:
                max_green = green

        while (' red' in l):
            red = int(l.split(' red')[0].split(' ')[-1])
            l = l.replace(' red','X',1)
            if red > max_red:
                max_red = red
        
        powers.append(max_red*max_blue*max_green)
    
    print(sum(powers))