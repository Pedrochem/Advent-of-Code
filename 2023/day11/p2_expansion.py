import numpy as np

def expand(lines):
    rows_to_expand = []
    columns_to_expand = []

    grid = np.array([list(line.rstrip()) for line in lines])
    grid_transpose = grid.T 

    # print(grid)
    print()
    print()
    # print(grid_transpose)
    print()
    print()

    for i,row in enumerate(grid):
        if '#' not in row:
            rows_to_expand.append(i)
    

    for j,column in enumerate(grid_transpose):
        if '#' not in column:
            columns_to_expand.append(j)

    return rows_to_expand, columns_to_expand


with open("full_input.txt") as f:
    lines = f.readlines()
    grid = np.array([list(line.rstrip()) for line in lines])
    extra_rows, extra_columns = expand(lines)
    print(extra_rows)

    galaxies = []
    for i,row in enumerate(grid):
        for j,val in enumerate(row):
            if val == '#':
                galaxies.append((i,j))


    distances = []
    for x,(curr_i,curr_j) in enumerate(galaxies):
        # print(f'Galaxy:{x}: {(curr_i,curr_j)}')
        y = x+1
        
        while y<len(galaxies):
            gal_i, gal_j = galaxies[y]
            dist = abs(curr_i-gal_i) + abs(curr_j-gal_j)
            for row in extra_rows:
                if curr_i > row > gal_i or gal_i > row > curr_i:
                    dist+=999999
            for column in extra_columns:
                if curr_j > column > gal_j or gal_j > column > curr_j:
                    dist+=999999
            # print(f'Dist galaxy {x} and {y}: {dist}')
        
            distances.append(dist)
            y+=1
    print(sum(distances))
