
def process_section(section):
    res = 0
    splits = section.split('mul(')
    for split in splits:
        x1 = 0
        x2 = 0
        find_first = False
        find_second = False
        find_comma = False
        find_mul = False

        for token in split:
            if token.isnumeric():
                if not find_first:
                    find_first = True
                    x1 = int(token)
                elif find_first and not find_comma:
                    x1 = x1 * 10 + int(token)
                elif find_first and find_comma:
                    if not find_second:
                        find_second = True
                        x2 = int(token)
                    else:
                        x2 = x2 * 10 + int(token)
            
            elif find_first and not find_comma and token==',':
                find_comma = True
            elif find_first and find_second and token == ')':
                find_mul = True
                break
            else:
                break
            
        if find_mul:
            res += x1*x2
    
    return res


with open('input.txt', 'r') as file:
    res = 0
    first = True
    lines = file.readlines()
    line = ''.join(lines)
    line = line.strip()
    sections = line.split('don\'t()')
    
    res += process_section(sections[0])
    for section in sections[1:]:
        i = 0
        if 'do()' in section:
            i = section.find('do()')
            res += process_section(section[i+4:])
print(res)


        


