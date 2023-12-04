# Part 1

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


with open("input.txt") as f:
    lines = f.readlines()
    products = []

    for l in lines:
        d1, d2 = 0, 0

        # finds first digit
        for i, li in enumerate(l):
            if li.isdigit() == True:
                d1 = li
                break

            for digit in digits.keys():
                if digit == l[i : i + len(digit)]:
                    d1 = str(digits[digit])
                    break
            else:
                continue
            break

        # finds last digit
        for i, li in enumerate(l[::-1]):
            if li.isdigit() == True:
                d2 = li
                break

            for digit in digits.keys():
                if digit[::-1] == l[::-1][i : i + len(digit)]:
                    d2 = str(digits[digit])
                    break
            else:
                continue
            break

        products.append(int(d1 + d2))

    print(sum(products))
