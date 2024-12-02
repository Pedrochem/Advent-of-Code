def check_inc(report, first):
    for i in range(len(report)-1):
        diff = int(report[i]) - int(report[i+1])
        if 1<= diff <=3:
            continue
        
        if first:
            if check_inc(report[:i]+report[i+1:], False):
                return True
            if check_inc(report[:i+1]+report[i+2:], False):
                return True
            return False
        else:
            return False
    
    return True
             
def check_dec(report, first):
    for i in range(len(report)-1):
        diff = int(report[i]) - int(report[i+1])
        if -3<= diff <=-1:
            continue
        
        if first:
            if check_dec(report[:i]+report[i+1:], False):
                return True
            if check_dec(report[:i+1]+report[i+2:], False):
                return True
            return False
        else:
            return False
    
    return True
    
    

     

with open('input.txt', 'r') as file:
    safe = 0
    for line in file:
        numbers = line.strip().split()

        if check_inc(numbers, True) or check_dec(numbers, True):
            # print(numbers)
            safe+=1
        
             

    print(safe)

    