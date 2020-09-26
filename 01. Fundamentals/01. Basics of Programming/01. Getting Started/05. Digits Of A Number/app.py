def getArrayOfDigits(n):
    current_number = n

    allDigits = []

    while current_number > 9:
        reminder = int(current_number % 10)
        allDigits.append(reminder)
        current_number = current_number / 10

    allDigits.append(int(current_number))

    return allDigits


n = int(input())
arrayOfDigits = getArrayOfDigits(n)

for i in range(len(arrayOfDigits) - 1, -1, -1):
    print(arrayOfDigits[i])
