from pprint import pprint
from itertools import product

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
    res = 0


    rows = len(lines)
    cols = len(lines[0])

    grid = [['' for _ in range(cols)] for _ in range(rows)]

    for i, line in enumerate(lines):
        for j, val in enumerate(line):
            grid[i][j] = val

    stop = False
    while not stop:
        stop=True
        pos_to_update = []

        for i in range(rows):
            for j in range(cols):
                
                if grid[i][j] != "@":
                    continue

                rp_neighbors = 0
                for dr, dc in product([1,0,-1], repeat=2):
                    if 0 <= dr+i < rows and 0 <= dc+j < cols and not (dc == 0 and dr == 0):
                        if grid[dr+i][dc+j] == "@":
                            rp_neighbors+=1

                if rp_neighbors < 4:
                    res+=1
                    pos_to_update.append((i,j))
                    stop=False
        
        for i,j in pos_to_update:
            grid[i][j] = "X"

    
    # pprint(grid)
    print(res)