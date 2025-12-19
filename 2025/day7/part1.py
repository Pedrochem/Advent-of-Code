

with open("inp.txt","r") as f:
    lines = [line.strip() for line in f.readlines()]
    start = lines[0].index('S')
    res = 0
    beams = [start]
    for line in lines[1:]:
        for beam in beams.copy():
            if line[beam] == "^":
                if beam-1 >= 0 and beam-1 not in beams:
                    beams.append(beam-1)
                if beam+1 < len(line) and beam+1 not in beams:
                    beams.append(beam+1)
                beams.remove(beam)
                res+=1
    print(res)




