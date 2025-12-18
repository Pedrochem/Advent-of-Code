

with open("input.txt","r") as f:
    f_size = 0
    col_size = {}
    total_res = 0

    for line in f:
        f_size+=1
        for i,col_num in enumerate(line.split()):
            if i not in col_size:
                col_size[i] = len(col_num)
            else:
                col_size[i] = max(col_size[i],len(col_num))    
    
    last_line = line
    print(last_line)

    col_symbol = {}
    res = [[0] * col_size[i] for i in range(len(last_line.split()))]

    
    f.seek(0)
   
    for i,symbol in enumerate(last_line.split()):
        col_symbol[i] = symbol
    
    for i, line in enumerate(f):

        if line == last_line:
            break
        
        last = 0
        for i in range(len(res)):
            for j in range(len(res[i])):
                if line[j+last] == " ":
                    continue
                res[i][j] = (int(res[i][j]) * 10) + int(line[j+last])
            last+=j+2 # skip whitespace

    total_res = 0
    for i in range(len(res)):
        symbol = col_symbol[i] 
        
        if symbol == "+":
            group_res = 0
        else:
            group_res = 1

        for j in range(len(res[i])):
            if symbol == '+':
                group_res+=res[i][j]
            else:
                group_res=group_res*res[i][j]
        
        total_res += group_res

   
    print(total_res)



