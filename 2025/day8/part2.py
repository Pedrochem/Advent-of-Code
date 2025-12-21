
from pprint import pprint
import heapq
from collections import Counter

def euclidian(p1,p2):
    x1,y1,z1 = map(int, p1.split(","))
    x2,y2,z2 = map(int, p2.split(","))

    res = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2 )**1/2

    return res

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

with open("inp.txt","r") as f:
    lines = [line.strip() for line in f.readlines()]
    dist = [[None] * len(lines) for _ in range(len(lines))]
    parent = [i for i in range(len(lines))]
    heap = []
    visited = set()

    for i, line in enumerate(lines):

        for j in range(i):
            dist[j][i] = euclidian(lines[j],lines[i])
            heapq.heappush(heap,(dist[j][i],i,j))

    while heap:
        dist, p1, p2 = heapq.heappop(heap)
        parent[find(p2)] = find(p1)
        if len(set(list(map(find,parent)))) == 1:
            res = int(lines[p1].split(",")[0])*int(lines[p2].split(",")[0])
            break

    print(res)
       




