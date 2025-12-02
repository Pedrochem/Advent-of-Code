
with open('input.txt', 'r') as file:

    res=0
    dial = 50
    prev_dial=50

    for line in file:
        direction = line[0]
        num = int(line[1:])
        
        if direction == "L":
            dial -= num
        elif direction == "R":
            dial+=num
        
        if dial <= 0 or dial >= 100:
            addon = abs(dial//100)
            res += addon
            if prev_dial == 0 and dial<0:
                res-=1

        if dial<=0 and dial%100==0:
            res+=1

        dial = dial % 100
        prev_dial = dial
        
        print(line.strip(), dial, res)

    print(res)
       

    


