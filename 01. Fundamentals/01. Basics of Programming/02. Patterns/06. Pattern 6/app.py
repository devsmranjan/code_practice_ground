def printPattern(n):
    row_length = n + 2
    # row_middle = int(row_length / 2)

    col_middle = int(n / 2)

    stars_each_side = int((row_length - 1) / 2)
    spaces = 1

    for i in range(n):
        row = ""

        for j in range(stars_each_side):
            row += "*\t"

        for s in range(spaces):
            row += "\t"

        for j in range(stars_each_side):
            row += "*\t"

        if i >= col_middle:
            stars_each_side += 1
        else:
            stars_each_side -= 1

        spaces = row_length - (2 * stars_each_side)

        print(row)


n = int(input())
printPattern(n)
