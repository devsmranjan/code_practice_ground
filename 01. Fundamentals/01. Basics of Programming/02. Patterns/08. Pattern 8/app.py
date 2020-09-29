def printPattern(n):
    for i in range(n):
        spaces = n - (i + 1)

        row = ""

        for s in range(spaces):
            row += "\t"

        row += "*"

        print(row)


n = int(input())
printPattern(n)
