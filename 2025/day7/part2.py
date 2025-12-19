

with open("inp.txt","r") as f:
    lines = [line.strip() for line in f.readlines()]
    start = lines[0].index('S')
    res = 0
    counter = 0
    cache = {}

    def travel(i,j):
        if (i,j) in cache:
            return cache[(i,j)]
        
        if lines[i][j] == ".":
            if i < len(lines)-1:
                return travel(i+1,j)
            return 1
        
        if j-1 >= 0:
            left = travel(i+1,j-1)
        if j+1 < len(lines):
            rigth = travel(i+1,j+1)

        cache[(i,j)] = left+rigth
        return left+rigth

    res = travel(1,start)
    print(res)




