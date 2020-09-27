def getLengthOfNumber(n):
    count = 0

    while n != 0:
        count += 1
        n = int(n / 10)

    return count


def getValue(n, k, lengthOfNumber):
    reminder = int(n % pow(10, k))
    cosent = int(n / pow(10, k))

    reversedValue = (reminder * pow(10, lengthOfNumber - k)) + cosent

    return reversedValue


def getRotatedNumber(n, k):
    rotatedNumber = 0
    lengthOfNumber = getLengthOfNumber(n)

    k = k % lengthOfNumber  # reduce the time of rotations

    if k > 0:
        rotatedNumber = getValue(n, k, lengthOfNumber)
    else:
        k = k + lengthOfNumber
        rotatedNumber = getValue(n, k, lengthOfNumber)

    return rotatedNumber


n = int(input())
k = int(input())

print(getRotatedNumber(n, k))
