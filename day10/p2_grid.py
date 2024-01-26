
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
    dim_x = len(lines)
    dim_y = len(lines[0])
    loop = [[symbol2coord[lines[i][j]] for j in range(dim_y)] for i in range(dim_x)]
    checkpoints = []

    def get_start_pos():
        for i in range(dim_x):
            for j in range(dim_y):
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

            
        if  (i+1,j) not in visited and i+1 < dim_x:
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

        if (i,j+1) not in visited and j+1 < dim_y:
            neigh_node = loop[i][j+1]
            if 'W' in neigh_node and 'E' in curr_node:
                route.append((i,j))
                j = j+1                
                continue
        
        # Dead end         
        i, j = route.pop()
    
    
    



coords = [[coord2symbol[loop[i][j]] for j in range(dim_y)] for i in range(dim_x)]

# for i in range(dim_x):
#     for j in range(dim_y):
#         print(coords[i][j],end='')
#     print()

# print()
# print()        

for i in range(dim_x):
    for j in range(dim_y):
        if (i,j) in route or coords[i][j]=='.' :
            print(coords[i][j],end='')
        else:
            print('.',end='')
            coords[i][j]='.'
    print()


print()
print()
print()

sorted_top = sorted(route, key=lambda x: x[0])
sorted_bot = sorted_top[::-1]

sorted_left = sorted(route, key=lambda x: x[1])
sorted_right = sorted_left[::-1]

# could optimize to check for next and prev pos
def get_tile_val(i,j):
    
    top_right, top_left = False, False
    bot_right, bot_left = False, False
    right_top, right_bot = False, False
    left_top, left_bot = False, False

    # check top
    for x, y in sorted_top:
        if y != j:
            continue

        if x >= i:
            break
        
        if (x,y-1) in route and 'E' in loop[x][y-1] and 'W' in loop[x][y]:
            top_left = True
        
        if (x,y+1) in route and 'W' in loop[x][y-1] and 'E' in loop[x][y]:
            top_right = True  

        if top_right and top_left:
            break


    # checks bot
    for x, y in sorted_bot:
        if y != j:
            continue

        if x <= i:
            break
        
        if (x,y-1) in route and 'E' in loop[x][y-1] and 'W' in loop[x][y]:
            bot_left = True
        
        if (x,y+1) in route and 'W' in loop[x][y-1] and 'E' in loop[x][y]:
            bot_right = True  

        if bot_right and bot_left:
            break    

    # checks right
    for x, y in sorted_right:
        if x != i:
            continue

        if y <= j:
            break
        
        if (x-1,y) in route and 'N' in loop[x-1][y] and 'S' in loop[x][y]:
            right_top = True
        
        if (x+1,y) in route and 'S' in loop[x+1][y] and 'N' in loop[x][y]:
            right_bot = True  

        if right_top and right_bot:
            break

    # checks left
    for x, y in sorted_left:
        if x != i:
            continue

        if y >= j:
            break
        
        if (x-1,y) in route and 'N' in loop[x-1][y] and 'S' in loop[x][y]:
            left_top = True
        
        if (x+1,y) in route and 'S' in loop[x+1][y] and 'N' in loop[x][y]:
            left_bot = True  

        if left_top and left_bot:
            break

    if top_right and top_left and bot_right and bot_left and right_top and right_bot and left_top and left_bot:
        return 'I'
    else:
        return 'O'



for i in range(dim_x):
    for j in range(dim_y):
        if coords[i][j] == '.':
            val = get_tile_val(i,j)
            coords[i][j] = val
            if val == "O":
                z=j
                #update left               
                while (z>0 and coords[i][z-1] in ('I','.','O')):
                    z-=1
                    coords[i][z] = 'O'

                z=j
                # update right
                while (z<dim_y-1 and coords[i][z+1] in ('I','.','O')):
                    z+=1
                    coords[i][z] = 'O'

                z=i
                # update top
                while (z>0 and coords[z-1][j] in ('I','.','O')):
                    z-=1
                    coords[z][j] = 'O'
                z=i
                # update bot
                while (z<dim_x-1 and coords[z+1][j] in ('I','.','O')):
                    z+=1
                    coords[z][j] = 'O'
                





res=0
for i in range(dim_x):
    for j in range(dim_y):
        if (i,j) in route or coords[i][j] in ('.','I','O') :
            if coords[i][j]=='I': res+=1
            print(coords[i][j],end='')
        else:
            print('/',end='')
    print()

print(res)