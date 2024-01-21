import math

symbol2coord = {
    '|' : ('N', 'S'),
    '-' : ('E', 'W'),
    'L' : ('N', 'E'),
    'J' : ('N', 'W'),
    '7' : ('S', 'W'),
    'F' : ('S', 'E'),
    '.' : ('.','.'),
    'S' : ('N','S','E','W') 
}

coord2symbol = {
    ('N', 'S'): '|',
    ('E', 'W'): '-',
    ('N', 'E'): 'L',
    ('N', 'W'): 'J',
    ('S', 'W'): '7',
    ('S', 'E'): 'F',
    ('.','.'): '.',
    ('N','S','E','W') : 'S'
    }



with open("full_input.txt") as f:

    checkpoints = {}
    lines = [line.rstrip() for line in f]
    dim = len(lines)
    loop = [[symbol2coord[lines[i][j]] for j in range(dim)] for i in range(dim)]
    checkpoints = []

    def get_start_pos():
        for i in range(dim):
            for j in range(dim):
                curr_node = loop[i][j]
                if curr_node == ('N','S','E','W'):
                    return i,j
            
    start_i,start_j = get_start_pos()
    i,j = start_i, start_j
    curr_node = ''
    prev_coord = ''
    
    visited = set()
    route = []
    first = True

    while loop[i][j] !=  ('N','S','E','W') or first:
        visited.add((i,j))
        first = False
        curr_node = loop[i][j]
        
        if len(route) > 2 and (start_i,start_j) in visited:
            visited.remove((start_i,start_j))
        else:
            visited.add((start_i,start_j))

        if (i-1,j) not in visited and i-1 >= 0:
            neigh_node = loop[i-1][j]
            if 'S' in neigh_node and 'N' in curr_node:
                route.append((i,j))
                i = i-1                
                continue

            
        if  (i+1,j) not in visited and i+1 < dim:
            neigh_node = loop[i+1][j]
            if 'N' in neigh_node and 'S' in curr_node:
                route.append((i,j))
                i = i+1                
                continue

        if (i,j-1) not in visited and j-1 >= 0:
            neigh_node = loop[i][j-1]
            if 'E' in neigh_node and 'W' in curr_node:
                route.append((i,j))
                j = j-1                
                continue

        if (i,j+1) not in visited and j+1 < dim:
            neigh_node = loop[i][j+1]
            if 'W' in neigh_node and 'E' in curr_node:
                route.append((i,j))
                j = j+1                
                continue
        
        # Dead end         
        i, j = route.pop()
    print(route)
    res = len(route)
    print(res)
    print(res/2)

# coords = [[coord2symbol[loop[i][j]] for j in range(dim)] for i in range(dim)]

# for i in range(dim):
#     for j in range(dim):
#         print(coords[i][j],end='')
#     print()

# res = math.ceil(main_loop_size/2)
# print(res)