
with open("full_input.txt") as f:
    lines = [line.rstrip() for line in f]
    next_value = 0
    for line in lines:
        hist = [int(x) for x in line.split()]
        new_seq = hist
        next_value += hist[-1]
        while (set(new_seq) != set([0])):
            new_seq =  [y-x for x,y in zip(new_seq[:-1],new_seq[1:])]
            next_value += new_seq[-1]

    print(next_value)
        