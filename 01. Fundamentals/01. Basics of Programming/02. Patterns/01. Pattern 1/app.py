def getPattern(n):
    for i in range(n):
        row = ""
        for j in range(i+1):
            row += "*\t"
        print(row)


n = int(input())
getPattern(n)
