



with open('input.txt', 'r') as file:
    safe = 0
    for line in file:
        numbers = line.strip().split()
        diffs = [int(numbers[i]) - int(numbers[i+1]) for i in range (len(numbers)-1)]
        
        if ((all(1<= diff <=3 for diff in diffs)) or (all(-3<= diff <=-1 for diff in diffs)) and 0 not in diffs):
            # print(numbers)
            # print("diffs: ", diffs)
            safe+=1


    print("Part 1:", safe)

