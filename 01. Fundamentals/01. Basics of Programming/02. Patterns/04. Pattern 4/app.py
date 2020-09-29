def printPattern(n):

    for i in range(n - 1, -1, -1):
        row = ""

        spaces = n - i - 1

        for space in range(spaces):
            row += "\t"

        for j in range(i+1):
            row += "*\t"

        print(row)


n = int(input())
printPattern(n)
