

with open("inp.txt","r") as f:
    f_size = 0
    for line in f:
        f_size+=1
        pass
    
    last_line = line
    print(last_line)

    col_symbol = {}
    res = [0] * len(last_line.split())

    f.seek(0)
    for i,symbol in enumerate(last_line.split()):
        col_symbol[i] = symbol
    
    for i, line in enumerate(f):
        if line == last_line:
            break
        
        for i,col_num in enumerate(line.split()):
            symbol = col_symbol[i]
            if symbol == "*" and res[i] == 0:
                res[i] = 1
            res[i] =  eval(f"{res[i]} {symbol} {col_num}")
   
    print(sum(res))



