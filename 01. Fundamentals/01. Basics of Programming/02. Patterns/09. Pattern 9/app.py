def printPattern(n):
    space_each_side = 0

    middle = int(n / 2)

    for i in range(n):
        row = ""

        space_in_between = n - (2 * space_each_side) - 1

        for s_s in range(space_each_side):
            row += "\t"

        row += "*"

        if space_in_between > 0:
            for s_b in range(space_in_between):
                row += "\t"

            row += "*"

        print(row)

        if i >= middle:
            space_each_side -= 1
        else:
            space_each_side += 1


n = int(input())
printPattern(n)
