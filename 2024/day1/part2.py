


from collections import defaultdict

with open('input.txt', 'r') as file:
    l1 = []
    l2 = defaultdict(int)

    for line in file:
        numbers = line.strip().split()
        l2[int(numbers[1])] += 1
        l1.append(int(numbers[0]))

    total_similarity= 0
    for i in l1:
        total_similarity += i * l2[i]

    print("Part 2:", total_similarity)
    
