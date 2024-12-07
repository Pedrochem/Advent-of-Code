from tqdm import tqdm

def get_next_guard_pos(guard_pos, guard_dir, saved_dirs):
    if (guard_pos, guard_dir) in saved_dirs:
        return -1,-1,False
    else:
        saved_dirs.add((guard_pos, guard_dir))

    i,j = tuple(a+b for a,b in zip(guard_pos,guard_dir))
   
    if not (0 <= i < rows and 0 <= j < cols):  # check exit
        return (0,0,True)
    
    

    if grid[i][j] == '#':
        return get_next_guard_pos(guard_pos, next_dir_map[guard_dir], saved_dirs)
    


    return ((i,j), guard_dir, False)


def can_escape(grid):
    guard_exited = False
    guard_pos = guard_initial_pos
    guard_dir = guard_initial_dir
    saved_dirs = set()

    while (not guard_exited):
        guard_pos, guard_dir, guard_exited = get_next_guard_pos(guard_pos, guard_dir, saved_dirs)
        if guard_pos == -1 and guard_dir == -1:
            return False

    return True




with open("input.txt","r") as f:
    grid = [list(line) for line in f.read().splitlines()]
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                guard_initial_pos = (i,j)
                break
        else:
            continue
        break


    print(f'Guard pos:{guard_initial_pos}')
    guard_exited = False
    guard_initial_dir = (-1,0)

    next_dir_map = {(-1,0): (0,1),
               (0,1): (1,0),
               (1,0): (0,-1),
               (0,-1): (-1,0),}


    possible = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.':
                grid[i][j] = '#'
                if not can_escape(grid): possible+=1 
                grid[i][j] = '.'
    
    print(possible)
   
        
        

        

