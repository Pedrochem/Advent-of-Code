


import heapq

with open('input.txt', 'r') as file:
    l1 = []
    l2 = []

    total_sum = 0
    for line in file:
        numbers = line.strip().split()
        heapq.heappush(l1, int(numbers[0]))
        heapq.heappush(l2, int(numbers[1]))

    for i in range(len(l1)):
        total_sum += abs(heapq.heappop(l1) - heapq.heappop(l2))

    print("Part 1:", total_sum)

