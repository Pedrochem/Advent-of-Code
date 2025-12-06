from pprint import pprint
from itertools import product

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
    ranges = []
    fresh=0
    fresh = set()
    for line in lines:
        if line == "":
            break
        a, b = map(int, line.split("-"))
        ranges.append((a,b))

    ranges.sort()

    merged = []
    for start, end in ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    res = sum(end - start + 1 for start, end in merged)

    print(res)