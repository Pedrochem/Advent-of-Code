with open("full_input.txt") as f:
    lines = [line.rstrip() for line in f]
    all_seeds = [int(s) for s in lines.pop(0).split(":")[1].strip().split()]
    seeds = list(zip(all_seeds[::2], all_seeds[1::2]))    
    new_seeds_list = []
    seeds_to_remove = set()
    seeds_to_update = {}
    seeds_to_add_immediately = []

    for line in lines:
        
        if line == "": continue

        if ':' in line: 
            # print("============================================")
            for s in seeds_to_remove: 
                seeds.remove(s)
            
            if len(new_seeds_list)>0: 
                seeds += new_seeds_list
            
            # print(f"Seeds: {seeds}")
            new_seeds_list = []
            seeds_to_remove = set()
            continue

        dest_start, src_start, src_range = map(int, line.split())
        src_end = src_start + (src_range-1)
        # print('---------------------------------------------------------------')
        # print(f"dest_start: {dest_start:02d} | src_start : {src_start:02d} | src_range: {src_range:02d}")

        for i, (seed_start, seed_range) in enumerate(seeds):
            seed_end = seed_start + (seed_range-1)
            # print(f'seed_start: {seed_start} | seed_range: {seed_range} | seed_end:{seed_start+seed_range-1}')
            
            # seed start in between src_start and src_end
            # TODO: probably fix
            if seed_start >= src_start and seed_start <= src_end:
                new_seed_start = seed_start - (src_start - dest_start)

                # seed end before source end
                if seed_end <= src_end:
                    new_seed_range = seed_range
                    
                    new_seeds_list.append((new_seed_start,new_seed_range))
                    seeds_to_remove.add((seed_start,seed_range))
                    continue

                # seed end after source end
                elif seed_end > src_end:
                    new_seed_range = seed_range - (seed_end - src_end)
                    extra_seed_start = seed_start + new_seed_range
                    extra_seed_range = seed_range - new_seed_range
                    
                    new_seeds_list.append((new_seed_start,new_seed_range))
                    seeds[i] = extra_seed_start,extra_seed_range
                    continue

            # seed start before src_start & seed end after src start
            if seed_start < src_start and seed_end >= src_start:
                
                # seed end before or equal to src end
                if seed_end <= src_end:
                    extra_seed_start = seed_start
                    extra_seed_range = src_start - seed_start

                    new_seed_start = dest_start
                    new_seed_range = seed_range - extra_seed_range
                    new_seeds_list.append((new_seed_start,new_seed_range))
                    seeds[i] = (extra_seed_start,extra_seed_range)
                    continue

                # seed end after src end
                elif seed_start + seed_range > src_start + src_range:
                    head_extra_seed_start = seed_start
                    head_extra_seed_range = (src_start - seed_start)

                    new_seed_start = dest_start
                    new_seed_range = src_range

                    tail_extra_seed_start = seed_start + (head_extra_seed_range + new_seed_range)
                    tail_extra_seed_range = seed_range - (head_extra_seed_range + new_seed_range)
                    
                    seeds[i] = (head_extra_seed_start,head_extra_seed_range)
                    new_seeds_list.append((new_seed_start,new_seed_range))
                    seeds_to_add_immediately.append((tail_extra_seed_start,tail_extra_seed_range))
                    continue
            
        if len(seeds_to_add_immediately)>0:
            seeds += seeds_to_add_immediately
        seeds_to_add_immediately = []
    
    for s in seeds_to_remove: 
        seeds.remove(s)

    if len(new_seeds_list)>0: 
        seeds += new_seeds_list

    print(f"Seeds: {seeds}")
    x = [x for x,_ in seeds]
    print(min(x))