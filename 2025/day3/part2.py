
with open('input.txt', 'r') as f:
    res = 0
    maxes = [0] + [None] * 11
    
    for line in f.readlines():
        line = line.strip()
        maxes = [0] + [None] * 11
        for i,n in enumerate(line):
            num = int(n)
            
            update = False
            
            for max_i,max_n in enumerate(maxes):
                if max_n is not None and num > max_n and (len(line) - (i+1)) >= (12 - (max_i+1)): 
                    update = True
                    break
            
            if update:
                maxes[max_i] = num
                j=max_i+1
                for i in range(j,len(maxes)):
                    maxes[i] = None
                continue
            
            
            for i in range(len(maxes)):
                if maxes[i] is None:
                    maxes[i] = num
                    break
            

        
        a=int("".join(str(x) for x in maxes))
        res+=a
    print(res)




