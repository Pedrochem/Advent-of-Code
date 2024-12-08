with open("input.txt","r") as f:
    lines = f.read().splitlines()
    res = 0

    for line in lines:
        target, rest = line.split(":")
        target = int(target)
        possible_sum = []

        rest =  [int(x) for x in rest.split()]
        
        first = True
        
        for x in rest:
            new_possible_sum = []
            added = False

            for i,ps in enumerate(possible_sum):
                if x + ps <= target:
                    new_possible_sum.append(x+ps)
                    added = True
                if x*ps <= target:
                    new_possible_sum.append(x*ps)
                    added = True
            
            possible_sum = new_possible_sum

            if first:
                possible_sum.append(x)
                added = True
                first = False

            if not added:
                break
                
        if target in possible_sum:
            res += target
    
    
    print(res)


           
