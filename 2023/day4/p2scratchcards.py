from collections import defaultdict

with open("input.txt") as f:
    lines = [line.rstrip() for line in f]
    res = 0
    games = defaultdict(int)

    for i, _ in enumerate(lines):
        games[i] = 1

    for i, line in enumerate(lines):
        matches = []
        numbers = line.split(":")[1]
        winning, guess = numbers.split("|")
        winning, guess = winning.split(), guess.split()

        matches = len([g for g in guess if g in winning])

        for j in range(i + 1, (i + matches) + 1):
            games[j] += games[i]

        # print(games)

    print(sum(games.values()))
