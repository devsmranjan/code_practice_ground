def getPattern(n):
    for i in range(n):
        spaces = n - (i+1)

        row = ""

        for space in range(spaces):
            row += "\t"

        for j in range(i+1):
            row += "*\t"

        print(row)


n = int(input())
getPattern(n)
