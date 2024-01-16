from collections import defaultdict

with open("input.txt") as f:
    lines = [line.rstrip() for line in f]
    all_seeds = [int(s) for s in lines.pop(0).split(":")[1].strip().split()]
    seeds = list(zip(all_seeds[::2], all_seeds[1::2]))

    seed_start, seed_range = 55, 16

    print("Seeds: ", seeds)

    for line in lines:
        if line == "" or ":" in line:
            print("============================================")
            continue

        dest_start, src_start, src_range = map(int, line.split())

        print(
            f"dest_start: {dest_start:02d} | src_start: {src_start:02d} | src_range: {src_range:02d}"
        )

        # seed start in between src_start and src_range
        if seed_start >= src_start and seed_start <= src_start + src_range:
            print("seed start in range")

            new_seed_start = seed_start - (src_start - dest_start)

            # seed end in before source end
            if seed_start + seed_range <= src_start + src_range:
                new_seed_range = seed_range

            # seed end after source end
            elif seed_start + seed_range > src_start + src_range:
                new_seed_range = seed_range - (
                    (seed_start + seed_range) - (src_start + src_range)
                )


                
                # TODO: might need to remove all -1 because of range
                extra_seed_start = seed_start + new_seed_range + 1
                extra_seed_range = seed_range - new_seed_range

        # seed start before src_start & seed end after src start
        if seed_start < src_start and seed_start + seed_range >= src_start:
            # seed end before or equal to src end
            if seed_start + seed_range <= src_start + src_range:
                extra_seed_start = seed_start
                extra_seed_range = (src_start - seed_start) - 1

                new_seed_start = dest_start
                new_seed_range = seed_range - extra_seed_range

            # seed end after src end
            elif seed_start + seed_range > src_start + src_range:
                head_extra_seed_start = seed_start
                head_extra_seed_range = (src_start - seed_start)

                new_seed_start = dest_start
                new_seed_range = src_range

                tail_extra_seed_start = seed_start + (head_extra_seed_range + new_seed_range)
                tail_extra_seed_range = seed_range - (head_extra_seed_range + new_seed_range)
                print()