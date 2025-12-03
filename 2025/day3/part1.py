
with open('input.txt', 'r') as f:
    res = 0
    max_1 = 0
    max_2 = None
    for line in f.readlines():
        line = line.strip()
        for i,n in enumerate(line):
            num = int(n)
            if num > max_1 and i < len(line)-1:
                max_1 = num
                max_2 = None
                continue
            
            if not max_2:
                max_2 = num

            if num > max_2:
                max_2 = num
        
        res+=int(str(max_1)+str(max_2))
        max_1 = 0
        max_2 = None
    print(res)




