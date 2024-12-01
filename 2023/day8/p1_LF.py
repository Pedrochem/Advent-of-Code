import itertools

def nodes_end(nodes):
    for n in nodes:
        if n[-1] != 'Z':
            return False
    return True

with open("full_input.txt") as f:
    lines = [line.rstrip() for line in f]
    inst = lines.pop(0)

    print(f'inst: {inst}')
    all_nodes = {}
    start_nodes = []
    for line in lines[1:]:
        node = line[:3]
        l = line[7:10]
        r = line[12:15]

        all_nodes[node] = (l,r)
        if node[-1] == 'A':
            start_nodes.append(node)
        
        # print(f'node: {node}')
        # print(f'left: {l}')
        # print(f'right: {r}')

    inst = [*inst]
    inst_cycle = itertools.cycle(inst)
    
    steps = 0
    cycles = []
    for curr_node in start_nodes:
        steps=0
        while (curr_node[-1] != 'Z'):
                inst = inst_cycle.__next__()
                if inst == 'L':
                    curr_node = all_nodes[curr_node][0]
                elif inst == 'R':
                    curr_node = all_nodes[curr_node][1]
                steps+=1
        cycles.append(steps)

    
    

    from functools import reduce
    import math
    
    def lcm(numbers):
        return reduce(lambda x, y: x * y // math.gcd(x, y), numbers, 1)
    
    print("LCM of", cycles, "is", lcm(cycles))