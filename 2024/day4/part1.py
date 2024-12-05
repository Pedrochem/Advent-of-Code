
def check_right(i,j):
    try:
       if "".join(lines[i][j] + lines[i][j+1] + lines[i][j+2] + lines[i][j+3]) == 'XMAS':
           return True
    except:
        return False
    return False    

def check_left(i,j):
    if j < 3:
        return False
    try:
       if "".join(lines[i][j] + lines[i][j-1] + lines[i][j-2] + lines[i][j-3]) == 'XMAS':
           return True
    except:
        return False
    return False    

def check_up(i,j):
    if i < 3:
        return False
    try:
       if "".join(lines[i][j] + lines[i-1][j] + lines[i-2][j] + lines[i-3][j]) == 'XMAS':
           return True
    except:
        return False
    return False    

def check_bot(i,j):
    try:
       if "".join(lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j]) == 'XMAS':
           return True
    except:
        return False
    return False    

def check_up_right(i,j):
    if i < 3:
        return False
    try:
       if "".join(lines[i][j] + lines[i-1][j+1] + lines[i-2][j+2] + lines[i-3][j+3]) == 'XMAS':
           return True
    except:
        return False
    return False    

def check_up_left(i,j):
    if i < 3 or j < 3:
        return False
    try:
       if "".join(lines[i][j] + lines[i-1][j-1] + lines[i-2][j-2] + lines[i-3][j-3]) == 'XMAS':
           return True
    except:
        return False
    return False    

def check_bot_right(i,j):
    try:
       if "".join(lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3]) == 'XMAS':
           return True
    except:
        return False
    return False    

def check_bot_left(i,j):    
    if j<3:
        return False
    try:
       if "".join(lines[i][j] + lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3]) == 'XMAS':
           return True
    except:
        return False
    return False    

with open("input.txt",'r') as f:
    word_count = 0
    lines = f.read().splitlines() 
    lines = [list(line) for line in lines]



    rows = len(lines)
    cols = len(lines[0])

    for i in range(rows):
        for j in range(cols):
            if check_right(i,j):
                word_count += 1
            if check_left(i,j):
                word_count += 1
            if check_up(i,j):
                word_count += 1
            if check_bot(i,j):
                word_count += 1
            if check_up_right(i,j):
                word_count += 1
            if check_up_left(i,j):
                word_count += 1
            if check_bot_right(i,j):
                word_count += 1
            if check_bot_left(i,j):
                word_count += 1

    print(word_count)

