


with open("input.txt",'r') as f:
    word_count = 0
    lines = f.read().splitlines() 
    lines = [list(line) for line in lines]



    rows = len(lines)
    cols = len(lines[0])

    for i in range(1,rows-1):
        for j in range(1,cols-1):
            if lines[i][j] == 'A':
                if set(lines[i-1][j-1] + lines[i+1][j+1]) == set(['M','S']):
                    if set(lines[i-1][j+1] + lines[i+1][j-1]) == set(['M','S']):
                        word_count += 1


            

    print(word_count)
    


