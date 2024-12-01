import numpy as np

def expand(lines):
    rows_to_expand = []
    columns_to_expand = []

    grid = np.array([list(line.rstrip()) for line in lines])
    grid_transpose = grid.T 


    print(grid)
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

    # print(rows_to_expand)
    # print(columns_to_expand) 

    grid_expanded = np.insert(grid,rows_to_expand,['.'*len(grid)],axis=0)
    grid_expanded = np.insert(grid_expanded,columns_to_expand,'.'*len(grid_expanded[0]),axis=1)

    print(grid_expanded)
    return grid_expanded


with open("input.txt") as f:
    grid = expand(f.readlines())
    galaxies = []
    for i,row in enumerate(grid):
        for j,val in enumerate(row):
            if val == '#':
                galaxies.append((i,j))

    print(galaxies)

    distances = []
    for x,(curr_i,curr_j) in enumerate(galaxies):
        print(f'Galaxy:{x}: {(curr_i,curr_j)}')
        y = x+1
        
        while y<len(galaxies):
            gal_i, gal_j = galaxies[y]
            dist = abs(curr_i-gal_i) + abs(curr_j-gal_j)
            print(f'Dist galaxy {x} and {y}: {dist}')
            distances.append(dist)
            y+=1
        break
        
    print(sum(distances))
