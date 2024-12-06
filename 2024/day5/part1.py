
from collections import defaultdict

with open("input.txt",'r') as f:
    lines = f.read().splitlines() 
    required_prevs = defaultdict(list)

    for i, line in enumerate(lines):
        if line == '':
            break
        first, second = line.split('|')
        required_prevs[second].append(first)

    correct=0
    res = 0

    for line in lines[i+1:]:
        nums = [x.strip() for x in line.split(',')]
        blocked = set()
        failed = False

        for n in nums:
            if n not in blocked:
                blocked.update(required_prevs[n])
            else:
                failed = True
                break

        if not failed:
            correct+=1
            res += int(nums[len(nums)//2] )
            
    print(res)


    
  

            

    