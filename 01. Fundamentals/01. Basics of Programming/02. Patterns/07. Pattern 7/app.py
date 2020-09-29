def printPattern(n):

    for i in range(n):
        row = ""

        for s in range(i):
            row += "\t"

        row += "*"

        print(row)


n = int(input())
printPattern(n)
