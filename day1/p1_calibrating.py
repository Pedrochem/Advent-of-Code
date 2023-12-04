# Part 1
with open("input.txt") as f:
    lines = f.readlines()
    products = []

    for l in lines:
        d1, d2 = 0, 0

        # finds first digit
        for li in l:
            if li.isdigit() == True:
                d1 = li
                break

        for li in l[::-1]:
            if li.isdigit() == True:
                d2 = li
                break

        products.append(int(d1 + d2))

    print(sum(products))
