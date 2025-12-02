
with open('input.txt', 'r') as file:

    res=0
    dial = 50
    
    for line in file:
        direction = line[0]
        num = int(line[1:])
        
        if direction == "L":
            dial -= num
        elif direction == "R":
            dial+=num
        dial = dial % 100

        if dial == 0:
            res+=1
        
        
    print(res)
       

    


