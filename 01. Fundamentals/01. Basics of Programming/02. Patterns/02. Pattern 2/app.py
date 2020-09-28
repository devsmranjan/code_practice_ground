def getPattern(n):
    for i in range(n, 0, -1):
        row = ""
        for j in range(i):
            row += "*\t"
        print(row)


n = int(input())
getPattern(n)
