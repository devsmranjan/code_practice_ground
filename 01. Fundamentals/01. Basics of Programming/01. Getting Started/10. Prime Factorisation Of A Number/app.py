def getPrimeFactors(n):
    primeFactors = []
    div = 2

    while div * div <= n:
        while n % div == 0:
            n = n / div
            primeFactors.append(div)
        div += 1

    if n != 1:
        primeFactors.append(int(n))

    return primeFactors


n = int(input())
primeFactors = getPrimeFactors(n)
print(*primeFactors)
