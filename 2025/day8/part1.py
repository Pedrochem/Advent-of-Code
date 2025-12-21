
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

    i=1000
    while i>0:
        dist, p1, p2 = heapq.heappop(heap)
        parent[find(p2)] = find(p1)
        print(lines[p1],lines[p2])
        i-=1
    
    res = 1
    print(list(map(find,parent)))

    for value, count in Counter(find(x) for x in parent).most_common(3):
        res = res * count

    print(res)
       




