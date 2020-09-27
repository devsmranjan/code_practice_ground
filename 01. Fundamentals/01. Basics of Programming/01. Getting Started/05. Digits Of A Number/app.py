def getArrayOfDigits(n):
    allDigits = []

    while n != 0:
        reminder = int(n % 10)
        allDigits.append(reminder)
        n = int(n / 10)

    return allDigits


n = int(input())
arrayOfDigits = getArrayOfDigits(n)

for i in range(len(arrayOfDigits) - 1, -1, -1):
    print(arrayOfDigits[i])
