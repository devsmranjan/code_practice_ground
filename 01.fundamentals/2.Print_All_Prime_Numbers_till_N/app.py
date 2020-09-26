def isPrime(n):
    d = 2

    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def getPrimeNumbers(low, high):
    allNumbers = []

    for i in range(low, high + 1):
        if i <= 2:
            allNumbers.append(i)
        elif i > 2 and i % 2 != 0:
            if (isPrime(i)):
                allNumbers.append(i)

    return allNumbers


low = int(input())
high = int(input())

allPrimeNumbers = getPrimeNumbers(low, high)
print(*allPrimeNumbers, sep="\n")
