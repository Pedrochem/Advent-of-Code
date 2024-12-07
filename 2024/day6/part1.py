
def get_next_guard_pos(guard_pos, guard_dir):
    i,j = tuple(a+b for a,b in zip(guard_pos,guard_dir))
   
    if not (0 <= i < rows and 0 <= j < cols):  # check exit
        return (0,0,True)
    
    if grid[i][j] == '#':
        return get_next_guard_pos(guard_pos, next_dir_map[guard_dir])
    

    return ((i,j), guard_dir, False)


with open("input.txt","r") as f:
    grid = f.read().splitlines()
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                guard_pos = (i,j)
                break
        else:
            continue
        break


    print(f'Guard pos:{guard_pos}')
    guard_exited = False
    guard_dir = (-1,0)

    next_dir_map = {(-1,0): (0,1),
               (0,1): (1,0),
               (1,0): (0,-1),
               (0,-1): (-1,0),}


    visited = set()
    while (not guard_exited):
        visited.add(guard_pos)
        guard_pos, guard_dir, guard_exited = get_next_guard_pos(guard_pos, guard_dir)
        
    print(len(visited))
        
        

        

