with open('input.txt', 'r') as file:
    res = 0
    for line in file:
        splits = line.strip().split('mul(')
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



        print(res)