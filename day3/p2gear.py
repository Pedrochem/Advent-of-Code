from collections import defaultdict

with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

    gears_dic = defaultdict(list)
    results = []
    for line_i,line in enumerate(lines):
        i=0
        while i < len(line):
            ok = False
            if line[i].isnumeric():

                n = line[i]
                while(len(line)>i+1 and line[i+1].isnumeric()):
                    i += 1
                    n += line[i]
            
                # check right
                if len(line) > i+1 and not line[i+1].isnumeric() and line[i+1] != '.':
                    gears_dic[(line_i,i+1)].append(int(n))
                    ok = True
        
                # check left 
                if i-len(n) != -1 and not line[i-len(n)].isnumeric() and line[i-len(n)] != '.':
                    gears_dic[(line_i,i-len(n))].append(int(n))
                    ok = True

                # check top:
                if line_i != 0:

                    # checks right diagonal
                    if len(line) > i+1 and not lines[line_i-1][i+1].isnumeric() and lines[line_i-1][i+1] != '.':
                        gears_dic[(line_i-1,i+1)].append(int(n))
                        ok = True

                    # check left diagonal
                    if i-len(n) != -1 and not lines[line_i-1][i-len(n)].isnumeric() and lines[line_i-1][i-len(n)] != '.':
                        gears_dic[(line_i-1,i-len(n))].append(int(n))
                        ok = True

                    for j in range(i-len(n)+1,i+1):
                        if not lines[line_i-1][j].isnumeric() and lines[line_i-1][j] != '.':
                            gears_dic[(line_i-1,j)].append(int(n))
                            ok = True
                
                # check botton:
                if line_i != len(lines)-1:

                    # checks right diagonal
                    if len(line) > i+1 and not lines[line_i+1][i+1].isnumeric() and lines[line_i+1][i+1] != '.':
                        gears_dic[(line_i+1,i+1)].append(int(n))
                        ok = True

                    # check left diagonal
                    if i-len(n) != -1 and not lines[line_i+1][i-len(n)].isnumeric() and lines[line_i+1][i-len(n)] != '.':
                        gears_dic[(line_i+1,i-len(n))].append(int(n))
                        ok = True
                    
                    for j in range(i-len(n)+1,i+1):
                        if not lines[line_i+1][j].isnumeric() and lines[line_i+1][j] != '.':
                            gears_dic[(line_i+1,j)].append(int(n))
                            ok = True             
        

            i+=1
    for key, val in gears_dic.items():
        if len(val)==2:
            results.append(val[0]*val[1])

    
    print(sum(results))