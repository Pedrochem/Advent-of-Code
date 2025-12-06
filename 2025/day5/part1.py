from pprint import pprint
from itertools import product

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
    ingredient = False
    ranges = []
    fresh=0
    for line in lines:
        if line == "":
            ingredient = True
            continue

        if not ingredient:
            r_start, r_end = [float(x) for x in line.split("-")]
            ranges.append((r_start,r_end))

        else:
           for r_start, r_end in ranges:
               if r_start <= float(line) <= r_end:
                   fresh+=1
                   break

    print(fresh)