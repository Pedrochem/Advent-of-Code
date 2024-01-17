with open("a.txt") as f:
    lines = [line.rstrip() for line in f]
    all_seeds = [int(s) for s in lines.pop(0).split(":")[1].strip().split()]
    seeds = list(zip(all_seeds[::2], all_seeds[1::2]))    
    new_seeds_list = []
    seeds_to_remove = []
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
            seeds_to_remove = []
            continue

        dest_start, src_start, src_range = map(int, line.split())
        # print('---------------------------------------------------------------')
        # print(f"dest_start: {dest_start:02d} | src_start : {src_start:02d} | src_range: {src_range:02d}")

        for seed_start, seed_range in seeds:
            # print(f'seed_start: {seed_start} | seed_range: {seed_range} | seed_end:{seed_start+seed_range-1}')
            # seed start in between src_start and src_end
            if seed_start >= src_start and seed_start <= src_start + src_range:
                new_seed_start = seed_start - (src_start - dest_start)

                # seed end in before source end
                if seed_start + seed_range <= src_start + src_range:
                    new_seed_range = seed_range
                    new_seeds_list.append((new_seed_start,new_seed_range))

                # seed end after source end
                elif seed_start + seed_range > src_start + src_range:
                    new_seed_range = seed_range - ((seed_start + seed_range) - (src_start + src_range))
                    extra_seed_start = seed_start + new_seed_range
                    extra_seed_range = seed_range - new_seed_range
                    new_seeds_list.append((new_seed_start,new_seed_range))
                    new_seeds_list.append((extra_seed_start,extra_seed_range))
                
                if (seed_start,seed_range) not in seeds_to_remove: 
                    seeds_to_remove.append((seed_start,seed_range))

            # seed start before src_start & seed end after src start
            if seed_start < src_start and seed_start + seed_range >= src_start:
                # seed end before or equal to src end
                if seed_start + seed_range <= src_start + src_range:
                    extra_seed_start = seed_start
                    extra_seed_range = src_start - seed_start

                    new_seed_start = dest_start
                    new_seed_range = seed_range - extra_seed_range
                    new_seeds_list.append((new_seed_start,new_seed_range))
                    new_seeds_list.append((extra_seed_start,extra_seed_range))

                # seed end after src end
                elif seed_start + seed_range > src_start + src_range:
                    head_extra_seed_start = seed_start
                    head_extra_seed_range = (src_start - seed_start)

                    new_seed_start = dest_start
                    new_seed_range = src_range

                    tail_extra_seed_start = seed_start + (head_extra_seed_range + new_seed_range)
                    tail_extra_seed_range = seed_range - (head_extra_seed_range + new_seed_range)
                    new_seeds_list.append((head_extra_seed_start,head_extra_seed_range))
                    new_seeds_list.append((new_seed_start,new_seed_range))
                    new_seeds_list.append((tail_extra_seed_start,tail_extra_seed_range))
                
                if (seed_start,seed_range) not in seeds_to_remove: 
                    seeds_to_remove.append((seed_start,seed_range))
            x=0
    print(f"Seeds: {seeds}")
    x = [x for x,_ in seeds]
    print(min(x))