
with open('input.txt', 'r') as f:
    ranges = []
    res = 0
    for line in f.readlines():
        line = line.strip()
        for split in line.split(","):
            if split:
                ranges.append((split.split("-")))


    for r1, r2 in ranges:
        if len(r1) % 2 != 0:
            r1 = "1" + "0"*len(r1)
        
        if int(r1)>int(r2):
            continue
    
        m1_r1, m2_r1 = r1[:len(r1)//2], r1[len(r1)//2:]

        if int(m2_r1) > int(m1_r1):
            m1_r1 = str(int(m1_r1)+1)
        
        if int(m1_r1+m2_r1) > int(r2):
            continue
        
        # ready to start
        n1, n2 = int(m1_r1+m1_r1), int(r2)
        while n1 <= n2:     
            res+=n1
            m1_r1 = str(int(m1_r1)+1)   
            n1 = int(m1_r1+m1_r1)
            
    print(res)




