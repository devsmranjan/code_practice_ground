def printPattern(n):
    middle = int(n / 2)
    stars = 1
    spaces = middle
    
    for i in range(n):
        row = ""

        for space in range(spaces):
            row += "\t"

        for j in range(stars):
            row += "*\t"
        
        print(row)

        if i >= middle:
            spaces += 1
        else:
            spaces -= 1

        stars = n - (2 * spaces)



n = int(input())
printPattern(n)
