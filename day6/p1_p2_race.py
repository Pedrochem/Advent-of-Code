import numpy as np

with open("full_input.txt") as f:
    lines = [line.rstrip() for line in f]
    times = [int(t.strip()) for t in lines[0].split("Time:")[1].split()]
    distances = [int(t.strip()) for t in lines[1].split("Distance:")[1].split()]
    
    races = list(zip(times,distances))
    possible_wins = []
    
    print(races)

    for time, distance in races:
        options = time+1
        wins = 0
        for hold_time in range(time)[1:]:
            ht_distance = hold_time * (time - hold_time)
            if ht_distance > distance:
                wins+=1
        
        possible_wins.append(wins)
        
    print(np.prod(possible_wins))


    