
def get_record(springs):
    record = []
    broken_count=0
    for spr in springs:
        if spr=='#':
            broken_count+=1
        if spr=='.':
            if broken_count>0:
                record.append(broken_count)
            broken_count=0 
    if broken_count>0:
        record.append(broken_count)
    return record


def get_possible_springs(springs,record):
    possible_springs = [springs]
    completed = []

    for i,spr in enumerate(springs):
        if spr == '?':
            curr_size = len(possible_springs)
            x=0
            while (x<curr_size):
                pos1 = possible_springs[x][:i]+'#'+possible_springs[x][i+1:]
                pos2 = possible_springs[x][:i]+'.'+possible_springs[x][i+1:]
                possible_springs.append(pos1)
                possible_springs.append(pos2)

                if not '?' in pos1:
                    completed.append(pos1)
                    completed.append(pos2)
                
                x+=1

    return completed


with open("full_input.txt") as f:
    lines = [line.rstrip() for line in f]
    possibilities=0
    for line in lines[:]:
        poss=0

        springs, record = line.split()
        record = [int(x) for x in record.split(',')]
        
        possible_springs = get_possible_springs(springs,record)
        for pr in possible_springs:
            if get_record(pr) == record:
                poss+=1
        
        possibilities+=poss

        print(springs,poss)
    
    print(possibilities)
