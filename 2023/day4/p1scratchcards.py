from collections import defaultdict

with open("test.txt") as f:
    lines = [line.rstrip() for line in f]
    res = 0
    games = defaultdict(list)

    print(games)

    for line in lines:
        matches = []
        numbers = line.split(":")[1]

        winning, guess = numbers.split("|")

        winning, guess = winning.split(), guess.split()

        matches = [g for g in guess if g in winning]

        # print(matches)
        if len(matches) > 0:
            res += 2 ** (len(matches) - 1)

    print(res)
