from collections import defaultdict



def check_ant(ant):
    return 0 <= ant[0] < rows and 0 <= ant[1] < cols  

grid = [list(line.strip()) for line in open("input.txt",'r')]

rows = len(grid)
cols = len(grid[0])

antennas = defaultdict(list)

for i in range(rows):
    for j in range(cols):
        if grid[i][j] != '.':
            antennas[grid[i][j]].append((i,j))



antinodes = set()
for ant, locs in antennas.items():
    for i,x_y in enumerate(locs):
        x,y = x_y
        print(f"Antenna {ant} pos: {i,j}")

        for n_x, n_y in locs[i+1:]:
            diff = (n_x - x, n_y - y)
            
            ant1 = (x - diff[0], y - diff[1])
            ant2 = (n_x + diff[0], n_y + diff[1])
            
            if check_ant(ant1):
                antinodes.add(ant1)
            if check_ant(ant2):
                antinodes.add(ant2)

print(len(antinodes))





