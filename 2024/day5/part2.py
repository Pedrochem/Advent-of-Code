from collections import defaultdict

def check_nums(nums, error):
    blocked = set()
    get_add_pos = {}
    for i, n in enumerate(nums):
        if n not in blocked:
            blocked.update(required_prevs[n])
            for rp in required_prevs[n]:
                get_add_pos[rp] = i
        else:
            nums[i], nums[get_add_pos[n]] = nums[get_add_pos[n]], nums[i]
            return check_nums(nums, True)
    
    if not error:
        return 0
    return int(nums[len(nums)//2] )
   
            

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
        res += check_nums(nums, False)
        
    print(res)


    
  

            

    