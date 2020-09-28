def getBulbs(n):

    # NOTE: All perfect squares having odd number of factors

    div = 1
    turnedOnBulbes = []

    while div * div <= n:
        turnedOnBulbes.append(pow(div, 2))
        div += 1

    return turnedOnBulbes


n = int(input())
bulbs = getBulbs(n)
print(*bulbs, sep="\n")
