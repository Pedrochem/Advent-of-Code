
with open("full_input.txt") as f:
    lines = [line.rstrip() for line in f]
    res=0
    for line in lines[:]:
        hist = [int(x) for x in line.split()]
        new_seq = hist
        next_values = [hist[0]]
        # print(next_values)
        while (set(new_seq) != set([0])):
            new_seq =  [y-x for x,y in zip(new_seq[:-1],new_seq[1:])]
            next_values.append(new_seq[0])
            # print(new_seq[0])

        next_val = 0
        for v in next_values[::-1][1:]:
            next_val = v - next_val
            # print(v)
        
        # print(next_val)
        res+=next_val
    print(res)
